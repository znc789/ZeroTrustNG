from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import analytics, auth, dashboard, health
from app.core.config import settings

app = FastAPI(
    title="Zero Trust Network Guardian",
    description="AI-powered adaptive zero trust security framework for modern networks.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.api_prefix)
app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(dashboard.router, prefix=settings.api_prefix)
app.include_router(analytics.router, prefix=settings.api_prefix)


@app.get("/")
async def root():
    return {
        "app": settings.app_name,
        "status": "online",
        "principle": "Never Trust. Always Verify.",
        "version": "1.0.0",
    }
