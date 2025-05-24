"""Simple recommendation engine for matching voters with candidates."""

from typing import List, Dict

from .profiles import CandidateProfile


def recommend_candidates(profiles: List[CandidateProfile], preferences: Dict[str, str]) -> List[CandidateProfile]:
    """Return candidates ranked by how well they match voter preferences."""
    def score(profile: CandidateProfile) -> int:
        s = 0
        for issue, desired in preferences.items():
            if profile.policies.get(issue, "").lower() == desired.lower():
                s += 1
        return s

    ranked = sorted(profiles, key=score, reverse=True)
    return ranked
