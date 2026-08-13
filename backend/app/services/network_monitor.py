from typing import Dict, List


class NetworkMonitor:
    """High-level packet and flow analysis engine for suspicious network behavior."""

    @staticmethod
    def summarize_flows(flows: List[Dict[str, object]]) -> Dict[str, object]:
        total_packets = sum(int(flow.get("packets", 0)) for flow in flows)
        flagged = sum(1 for flow in flows if flow.get("suspicious", False))
        return {
            "total_packets": total_packets,
            "suspicious_flows": flagged,
            "top_protocols": ["TCP", "DNS", "HTTPS"],
            "status": "observing",
        }

    @staticmethod
    def detect_anomalies(flow: Dict[str, object]) -> Dict[str, object]:
        detection = "normal"
        if flow.get("dst_port") in {22, 23, 445} and flow.get("count", 0) > 20:
            detection = "brute_force"
        if flow.get("protocol") == "dns" and flow.get("query_length", 0) > 80:
            detection = "dns_tunneling"
        if flow.get("bytes_out", 0) > 500000 and flow.get("bytes_in", 0) < 3000:
            detection = "data_exfiltration"
        return {
            "event_type": detection,
            "severity": "high" if detection != "normal" else "low",
            "anomaly": detection != "normal",
        }
