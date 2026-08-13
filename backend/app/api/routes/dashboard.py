import random
from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard/overview")
async def dashboard_overview():
    live_users = 184 + random.randint(-12, 28)
    connected_devices = 912 + random.randint(-24, 44)
    active_threats = 42 + random.randint(-8, 10)
    risk_score = 32 + random.randint(-5, 16)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "live_users": live_users,
        "connected_devices": connected_devices,
        "threats_detected": active_threats,
        "risk_score": risk_score,
        "alerts": [
            {"id": "ALT-2049", "severity": "critical", "title": "Impossible travel detected", "source": "User: N. Voss"},
            {"id": "ALT-2050", "severity": "high", "title": "Malware beaconing", "source": "Host: win-srv-19"},
            {"id": "ALT-2051", "severity": "medium", "title": "Brute force against VPN gateway", "source": "IP: 203.0.113.22"},
        ],
        "widgets": {
            "users": live_users,
            "devices": connected_devices,
            "network": "stable",
            "mfa": 96,
        },
        "timeline": [
            {"name": "Mon", "value": 28},
            {"name": "Tue", "value": 34},
            {"name": "Wed", "value": 39},
            {"name": "Thu", "value": 46},
            {"name": "Fri", "value": 52},
            {"name": "Sat", "value": 41},
            {"name": "Sun", "value": 38},
        ],
        "heatmap": [
            {"region": "US East", "risk": 82},
            {"region": "US West", "risk": 64},
            {"region": "EU", "risk": 58},
            {"region": "APAC", "risk": 76},
            {"region": "LATAM", "risk": 48},
        ],
        "posture": [
            ["Identity verification", 96],
            ["Device trust", 91],
            ["Network segmentation", 88],
            ["Adaptive policy", 93],
        ],
    }
