# Stage 1: Build & Verification Stage
FROM python:3.11-slim AS builder

WORKDIR /build

# Install dependencies into user directory
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy source and run tests inside the build container
COPY . .
RUN python -m unittest discover -s tests -p "test_*.py" -v

# Stage 2: Minimal, Hardened Production Runtime
FROM python:3.11-slim AS runtime

WORKDIR /app

# Create unprivileged service user for security
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -s /bin/bash -m appuser

# Copy installed dependencies and source code
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appgroup src/ /app/src/

ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8080

CMD ["python", "-m", "src.app"]
