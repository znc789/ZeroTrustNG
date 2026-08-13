class DeviceTrustEngine:
    """Calculate trust score for connected endpoints."""

    @staticmethod
    def score(device: dict) -> int:
        os_score = 20 if device.get("os", "windows").lower() in {"windows", "linux", "macos"} else 8
        patch_score = 15 if device.get("patch_status") == "up_to_date" else 5
        antivirus_score = 15 if device.get("antivirus_status") == "healthy" else 3
        encryption_score = 10 if device.get("disk_encryption") else 2
        firewall_score = 10 if device.get("firewall_enabled") else 4
        usb_score = 10 if not device.get("usb_activity", False) else 2
        security_score = 15 if device.get("security_posture") == "strong" else 8

        total = os_score + patch_score + antivirus_score + encryption_score + firewall_score + usb_score + security_score
        return min(total, 100)

    @staticmethod
    def classification(score: int) -> str:
        if score >= 80:
            return "trusted"
        if score >= 60:
            return "limited"
        return "untrusted"
