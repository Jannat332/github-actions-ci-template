# Software Design Specification - GitHub Actions CI

## Workflow Specification (`.github/workflows/ci.yml`)

```yaml
name: Continuous Integration

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Static Code Analysis
        run: |
          python -m pip install --upgrade pip flake8
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Run Unit Tests
        run: |
          python -m unittest discover -s tests -p "test_*.py"

  docker-build:
    needs: [lint, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Container Image
        run: |
          docker build -t app:ci-${{ github.sha }} .
```

## Multi-Stage Container Design
```dockerfile
# Stage 1: Build & Verification
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt
COPY . .
RUN python -m unittest discover -s tests

# Stage 2: Minimal Production Runtime
FROM python:3.11-slim AS runtime
WORKDIR /app
# Create non-root user
RUN useradd -u 1001 appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /app/src /app/src
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser
CMD ["python", "-m", "src.app"]
```
