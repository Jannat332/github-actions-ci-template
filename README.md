# GitHub Actions CI & Docker Pipeline Template

A production-ready continuous integration (CI) and containerization template designed for modern web services and microservices.

---

## Features
- **Automated Matrix Testing**: Runs test suites automatically across Python versions (`3.10`, `3.11`) on every `push` and `pull_request`.
- **Static Code Hygiene**: Automated linting using `flake8` to catch syntax errors and undefined variables before merging.
- **Multi-Stage Dockerfile**: 
  - *Stage 1 (Builder)*: Installs dependencies and executes unit tests.
  - *Stage 2 (Runtime)*: Minimal, unprivileged non-root container (`appuser`) for enhanced production security.
- **One-Command Local Orchestration**: Replicate the exact CI environment locally with `docker compose up --build`.

---

## Project Structure
```
04-github-actions-ci-template/
├── .github/
│   └── workflows/
│       └── ci.yml               # Complete GitHub Actions CI pipeline
├── src/
│   └── app.py                   # Health & metrics service
├── tests/
│   └── test_app.py              # Automated unit tests
├── Dockerfile                   # Hardened multi-stage container build
├── docker-compose.yml           # Local multi-container orchestrator
├── .dockerignore                # Build cache exclusion rules
├── requirements.txt             # Application dependency list
├── arch.md                      # Pipeline architecture diagram
├── pwd.md                       # CI/CD product requirements & workflow
├── design.md                    # Workflow specs and Docker build stages
├── memory.md                    # Key architectural decisions & tradeoffs
├── rules.md                     # DevOps standards & security guidelines
└── bug-report.md                # Testing findings & resolved build issues
```

---

## Quickstart

### 1. Running Unit Tests Locally
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 2. Building the Docker Container
```bash
# Build the multi-stage image
docker build -t devops-app:latest .

# Run the container locally
docker run -p 8080:8080 devops-app:latest

# Verify health endpoint in another terminal
curl http://localhost:8080/health
```

### 3. Running via Docker Compose
```bash
docker compose up --build
```

---

## GitHub Actions Workflow Summary
1. **Lint Job**: Scans codebase with `flake8`.
2. **Test Job**: Runs `unittest` in parallel across Python 3.10 and 3.11 runners.
3. **Docker Build Job**: Builds the multi-stage image using Buildx caching after lint and test jobs succeed.

---

## License
MIT License.
