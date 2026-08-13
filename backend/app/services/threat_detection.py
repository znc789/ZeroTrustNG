from typing import Dict, List


class ThreatDetectionEngine:
    """Rule-based engine that maps suspicious activity to threat categories."""

    @staticmethod
    def detect_event(event: Dict[str, object]) -> Dict[str, object]:
        threat_type = "benign"
        severity = "low"

        if event.get("event_type") in {"port_scan", "bruteforce", "credential_stuffing"}:
            threat_type = "reconnaissance"
            severity = "high"
        elif event.get("event_type") == "beaconing":
            threat_type = "command_and_control"
            severity = "critical"
        elif event.get("event_type") == "data_exfiltration":
            threat_type = "data_exfiltration"
            severity = "critical"
        elif event.get("event_type") == "malware_download":
            threat_type = "malware"
            severity = "high"
        elif event.get("event_type") == "impossible_travel":
            threat_type = "credential_theft"
            severity = "high"

        return {
            "threat_type": threat_type,
            "severity": severity,
            "confidence": 0.9 if severity in {"high", "critical"} else 0.7,
            "mitre": ["T1059", "T1078", "T1046"],
        }

    @staticmethod
    def detect_batch(events: List[Dict[str, object]]) -> List[Dict[str, object]]:
        return [ThreatDetectionEngine.detect_event(event) for event in events]
