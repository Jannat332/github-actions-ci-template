# Memory & Decision Log - GitHub Actions CI

## Context & Key Decisions
- **Decision 1: Multi-Stage Dockerfile over Fat Single-Stage Image**
  - *Rationale*: Single-stage images leave build tools, compilers, test logs, and temporary caches in the final image, bloating size by hundreds of megabytes. Multi-stage builds copy only the compiled binaries/dependencies into a minimal runtime layer.
- **Decision 2: Matrix Testing across Multiple Minor Versions**
  - *Rationale*: A script that passes in Python 3.11 might fail on Python 3.10 due to newer syntax features (like pipe union types or specific standard library changes). Matrix jobs guarantee backwards compatibility.
- **Decision 3: Non-Root User Execution (`USER appuser`)**
  - *Rationale*: Running container workloads as `root` (the default in Docker) is a critical security vulnerability. If a vulnerability is exploited inside the container, running as an unprivileged user prevents host privilege escalation.
