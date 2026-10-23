"""FastAPI entry point (02 §2.2); each epic mounts its domain routers here."""

from fastapi import FastAPI

app = FastAPI(title="RepSight API")


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    """Liveness for the internal ALB (02 §8.5.1)."""
    return {"status": "ok"}


@app.get("/readyz")
async def readyz() -> dict[str, str]:
    """Readiness for the internal ALB (02 §8.5.1)."""
    # ponytail: nothing to check yet; ping Postgres and Valkey here once E1 adds their clients.
    return {"status": "ok"}
