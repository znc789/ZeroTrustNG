from typing import Dict, List


class IncidentResponseEngine:
    """SOAR-style automation layer for response playbooks."""

    @staticmethod
    def generate_playbook(threat_type: str) -> Dict[str, List[str]]:
        playbook = {
            "credential_theft": ["Lock user account", "Revoke active sessions", "Trigger MFA", "Review login history"],
            "malware": ["Quarantine endpoint", "Block outbound traffic", "Collect forensic snapshot", "Notify SOC"],
            "data_exfiltration": ["Block suspicious IPs", "Disable export paths", "Isolate host", "Review DLP events"],
            "brute_force": ["Rate-limit source", "Block IP", "Reset VPN users", "Monitor for spread"],
        }
        return {"threat_type": threat_type, "actions": playbook.get(threat_type, ["Escalate to SOC", "Open incident ticket"]) }

    @staticmethod
    def notify_channels(incidents: List[Dict[str, str]]) -> Dict[str, str]:
        return {
            "email": "soc@zerotrustng.local",
            "slack": "#soc-alerts",
            "teams": "ZeroTrust Guardian",
            "webhook": "https://example.internal/webhook",
        }
