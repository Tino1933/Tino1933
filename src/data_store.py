"""Simple JSON-based data store for candidate profiles."""

import json
from pathlib import Path
from typing import List

from .profiles import CandidateProfile

DATA_FILE = Path("data/candidates.json")


def save_profiles(profiles: List[CandidateProfile]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump([profile.__dict__ for profile in profiles], f, indent=2)


def load_profiles() -> List[CandidateProfile]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    profiles = [CandidateProfile(**item) for item in raw]
    return profiles
