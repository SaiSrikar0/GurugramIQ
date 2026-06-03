from __future__ import annotations

from fastapi import FastAPI

from .api.routes import router as api_router

app = FastAPI(
    title="Startup Validation API",
    version="0.1.0",
    description="FastAPI backend for startup analysis, CRUD, prediction, and competition insights.",
)

app.include_router(api_router)


@app.get("/", tags=["System"])
def root() -> dict[str, str]:
    return {"message": "Startup Validation API is running"}
