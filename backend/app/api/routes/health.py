from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "zero-trust-network-guardian",
        "checks": {
            "database": "pending",
            "redis": "pending",
            "ai": "ready",
        },
    }
