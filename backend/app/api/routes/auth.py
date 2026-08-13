from fastapi import APIRouter

router = APIRouter(tags=["auth"])


@router.post("/auth/login")
async def login():
    return {
        "access_token": "demo-token",
        "token_type": "bearer",
        "user": {
            "id": "u-1001",
            "name": "Nadia Voss",
            "role": "SOC Analyst",
            "risk_score": 18,
        },
    }


@router.get("/auth/me")
async def me():
    return {
        "id": "u-1001",
        "name": "Nadia Voss",
        "role": "SOC Analyst",
        "mfa_enabled": True,
        "continuous_auth": True,
        "device_trust": 94,
    }
