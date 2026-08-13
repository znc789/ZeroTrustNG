from fastapi import APIRouter

from app.services.ai_analytics import BehaviorAnalytics
from app.services.device_trust import DeviceTrustEngine
from app.services.network_monitor import NetworkMonitor
from app.services.risk_engine import RiskEngine
from app.services.threat_detection import ThreatDetectionEngine

router = APIRouter(tags=["analytics"])


@router.get("/analytics/behavior")
async def behavior_analysis():
    model = BehaviorAnalytics()
    return model.predict([
        {"hour": 9, "location": "us-east", "device_fingerprint": "corp-laptop-win11", "ip_reputation": "clean"},
        {"hour": 2, "location": "frankfurt", "device_fingerprint": "unknown-device", "ip_reputation": "suspicious"},
    ])


@router.get("/analytics/device-trust")
async def device_trust():
    device = {
        "os": "windows",
        "patch_status": "up_to_date",
        "antivirus_status": "healthy",
        "disk_encryption": True,
        "firewall_enabled": True,
        "usb_activity": False,
        "security_posture": "strong",
    }
    score = DeviceTrustEngine.score(device)
    return {"device_id": "dev-77", "score": score, "classification": DeviceTrustEngine.classification(score)}


@router.get("/analytics/network")
async def network_analysis():
    flow = {"protocol": "dns", "query_length": 120, "bytes_out": 620000, "bytes_in": 500, "dst_port": 53, "count": 30}
    return NetworkMonitor.detect_anomalies(flow)


@router.get("/analytics/risk")
async def risk_summary():
    assessment = RiskEngine.assess(68, 74, 83, 59, 76)
    return {"risk_level": assessment.risk_level, "overall_risk": assessment.overall_risk, "insights": assessment.insights}


@router.get("/analytics/threats")
async def threat_summary():
    event = {"event_type": "impossible_travel", "source_ip": "198.51.100.5", "device_id": "dev-991", "user_id": "u-1001"}
    return ThreatDetectionEngine.detect_event(event)
