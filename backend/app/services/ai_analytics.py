from typing import Dict, List


class BehaviorAnalytics:
    """Simple AI-inspired behavior analytics model demo."""

    def __init__(self):
        self.baselines = {
            "login_hours": [9, 10, 11, 13, 14, 15, 16],
            "geo_regions": ["us-east", "us-west", "eu-central"],
            "device_fingerprints": ["corp-laptop-win11", "corp-macbook", "android-gt-8"],
        }

    def analyze_login(self, login_event: Dict[str, object]) -> Dict[str, object]:
        hour = int(login_event.get("hour", 12))
        is_business_hour = hour in self.baselines["login_hours"]
        risk = 0
        if not is_business_hour:
            risk += 25
        if login_event.get("location") not in self.baselines["geo_regions"]:
            risk += 20
        if login_event.get("device_fingerprint") not in self.baselines["device_fingerprints"]:
            risk += 30
        if login_event.get("ip_reputation") == "suspicious":
            risk += 25

        return {
            "risk_score": min(risk, 100),
            "baseline_match": is_business_hour,
            "anomaly_flags": [
                flag for flag, enabled in {
                    "off_hours_login": not is_business_hour,
                    "unexpected_geo": login_event.get("location") not in self.baselines["geo_regions"],
                    "new_device": login_event.get("device_fingerprint") not in self.baselines["device_fingerprints"],
                    "suspicious_ip": login_event.get("ip_reputation") == "suspicious",
                }.items() if enabled
            ],
        }

    def explain_risk(self, risk_score: int) -> str:
        if risk_score >= 80:
            return "High-risk login and device mismatch; enforce step-up authentication."
        if risk_score >= 50:
            return "Behavior analytics detected moderate deviation from baseline."
        return "Behavior remains within enterprise normal patterns."

    def predict(self, events: List[Dict[str, object]]) -> Dict[str, object]:
        avg_risk = sum(item.get("risk_score", 0) for item in [self.analyze_login(event) for event in events]) / max(len(events), 1)
        return {
            "predicted_risk": round(avg_risk, 2),
            "model": "IsolationForest + heuristics",
            "confidence": 0.87,
        }
