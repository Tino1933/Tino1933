"""User personalization utilities."""

from typing import List, Dict

from .profiles import CandidateProfile


def match_candidates_by_district(profiles: List[CandidateProfile], district: str) -> List[CandidateProfile]:
    """Return candidates relevant to the provided district."""
    # Placeholder logic; real implementation would filter based on district info.
    return [p for p in profiles if district.lower() in p.name.lower() or not district]


def compare_candidates(c1: CandidateProfile, c2: CandidateProfile, issues: List[str]) -> Dict[str, Dict[str, str]]:
    """Return a side-by-side comparison of two candidates on given issues."""
    comparison = {}
    for issue in issues:
        comparison[issue] = {
            c1.name: c1.policies.get(issue, "N/A"),
            c2.name: c2.policies.get(issue, "N/A"),
        }
    return comparison
