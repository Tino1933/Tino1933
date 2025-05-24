from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class CandidateProfile:
    name: str
    photo_url: str
    party: str
    roles: List[str]
    policies: Dict[str, str]
    voting_record: Dict[str, str]
    funding_sources: List[str]
    recent_news: List[str]
    statements: List[str]

    def validate(self) -> bool:
        required_fields = [self.name, self.party]
        return all(bool(field) for field in required_fields)
