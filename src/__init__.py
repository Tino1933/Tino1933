"""Candidate information package."""

from .profiles import CandidateProfile
from .scraper import scrape_candidates
from .data_store import load_profiles, save_profiles
from .personalization import match_candidates_by_district, compare_candidates
from .recommendation import recommend_candidates

__all__ = [
    "CandidateProfile",
    "scrape_candidates",
    "load_profiles",
    "save_profiles",
    "match_candidates_by_district",
    "compare_candidates",
    "recommend_candidates",
]
