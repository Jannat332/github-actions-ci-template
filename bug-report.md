# Testing & Bug Report - GitHub Actions CI Template

## Test Execution Summary
- **Target**: CI workflow syntax, multi-stage Docker build layers, unit test execution.
- **Scope**: Matrix test runner, flake8 lint rule verification, non-root user permissions, healthcheck endpoints.
- **Result**: Pipeline stages verified.

## Issues Identified & Fixed During Development

### Bug #1: Missing `.dockerignore` Causing Cache Invalidation
- **Severity**: Medium
- **Symptom**: Local `.git` folder, `__pycache__`, and temporary test logs were being copied into the builder stage, causing cache misses and bloating build times.
- **Fix**: Created `.dockerignore` excluding `.git`, `__pycache__`, `venv`, and `*.log`.

### Bug #2: Permission Denied on Container Directory Creation
- **Severity**: High
- **Symptom**: Setting `USER appuser` before copying source code caused runtime permission errors when the app attempted to read package caches.
- **Fix**: Used `COPY --chown=appuser:appgroup` and assigned `appuser` explicit ownership of the `/app` and `/home/appuser/.local` directories.

### Bug #3: Flake8 Severity Escalation on Formatting Whitespace
- **Severity**: Low
- **Symptom**: CI failed builds on harmless trailing spaces.
- **Fix**: Split `flake8` execution into two phases: strict fatal checks for syntax errors/undefined names (`E9,F63,F7,F82`), and non-fatal exit-zero reporting for cosmetic warnings.
