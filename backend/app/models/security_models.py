from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ThreatEvent:
    event_id: str
    source_ip: str
    device_id: str
    user_id: str
    threat_type: str
    severity: str
    score: int
    metadata: Dict[str, object] = field(default_factory=dict)


@dataclass
class RiskAssessment:
    user_score: int
    device_score: int
    network_score: int
    behavior_score: int
    threat_score: int
    overall_risk: int
    risk_level: str
    insights: List[str] = field(default_factory=list)
