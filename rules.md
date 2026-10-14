# Engineering Rules & Guidelines - GitHub Actions CI

## 1. Principles
- **KISS**: Avoid third-party unverified marketplace actions that can introduce security supply-chain risks. Stick to official `actions/checkout@v4` and `actions/setup-python@v5`.
- **Fail Fast**: The `lint` and `test` jobs run before the heavy `docker-build` step (`needs: [lint, test]`), ensuring that syntax or test errors abort the workflow immediately without wasting expensive container build runner minutes.

## 2. Docker Best Practices
- Never use the `:latest` tag for base images in production; pin specific minor versions (`python:3.11-slim`).
- Order `Dockerfile` instructions from least frequently changed (`COPY requirements.txt`) to most frequently changed (`COPY . .`) to maximize Docker layer cache hits.
- Always include a `.dockerignore` file to prevent copying `.git`, local virtual environments, and temporary files into the container.
