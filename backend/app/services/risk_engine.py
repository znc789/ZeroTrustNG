from typing import Dict, List

from app.models.security_models import RiskAssessment


class RiskEngine:
    """Compute risk from user, device, network, and threat telemetry."""

    @staticmethod
    def assess(user_score: int, device_score: int, network_score: int, behavior_score: int, threat_score: int) -> RiskAssessment:
        overall = int((user_score * 0.25) + (device_score * 0.2) + (network_score * 0.25) + (behavior_score * 0.15) + (threat_score * 0.15))

        if overall >= 80:
            level = "critical"
        elif overall >= 60:
            level = "high"
        elif overall >= 35:
            level = "medium"
        else:
            level = "low"

        insights = []
        if user_score > 60:
            insights.append("User behavior deviates from baseline")
        if device_score < 50:
            insights.append("Device posture is below trust threshold")
        if network_score > 70:
            insights.append("Network telemetry shows suspicious connectivity")
        if threat_score > 65:
            insights.append("Active threat detections are increasing risk")

        return RiskAssessment(
            user_score=user_score,
            device_score=device_score,
            network_score=network_score,
            behavior_score=behavior_score,
            threat_score=threat_score,
            overall_risk=overall,
            risk_level=level,
            insights=insights or ["No material anomalies detected"],
        )

    @staticmethod
    def policy_recommendation(risk_level: str) -> Dict[str, List[str]]:
        recommendations = {
            "low": ["Continue standard policy", "Monitor for anomalies"],
            "medium": ["Require MFA revalidation", "Limit access to critical apps"],
            "high": ["Quarantine device", "Block high-risk IP ranges"],
            "critical": ["Disable session", "Escalate to incident response"],
        }
        return {"risk_level": risk_level, "actions": recommendations.get(risk_level, recommendations["low"]) }
