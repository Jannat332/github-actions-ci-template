# Project Workflow & Requirements (PWD) - GitHub Actions CI

## 1. Problem Statement
Manual code testing before merging pull requests leads to human error, regression bugs in production, and broken master branches. A standardized, automated CI workflow guarantees that every code commit is statically verified, unit tested, and containerized before merging.

## 2. Functional Requirements
- **FR-1 Event Triggers**: Trigger pipeline on `push` to `main`/`master` and all `pull_request` submissions.
- **FR-2 Automated Test Job**: Run test suites with zero human intervention and report step durations.
- **FR-3 Matrix Testing**: Verify compatibility across multiple Python versions (e.g. 3.10, 3.11).
- **FR-4 Multi-Stage Dockerfile**:
  - Stage 1: Build & test stage containing development tools.
  - Stage 2: Distroless or Alpine production image containing only runtime dependencies.
- **FR-5 Local Docker Compose**: Developers must be able to replicate the exact CI container build locally using `docker compose up --build`.

## 3. Non-Functional Requirements
- **Fast Execution**: Entire pipeline should complete in under 2 minutes.
- **Security**: Run containers as non-root users (`USER appuser`) to avoid container breakout vulnerabilities.
