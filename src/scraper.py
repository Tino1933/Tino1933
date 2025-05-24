"""Utilities for scraping data about political candidates."""

import requests
from bs4 import BeautifulSoup
from typing import List

from .profiles import CandidateProfile

# Example functions for scraping - these functions are placeholders and would
# need updating with real URLs and parsing logic.

USER_AGENT = {
    "User-Agent": "CandidateInfoBot/1.0 (+https://example.com)"
}

def fetch_page(url: str) -> str:
    """Fetch HTML content from a URL."""
    resp = requests.get(url, headers=USER_AGENT, timeout=10)
    resp.raise_for_status()
    return resp.text

def parse_candidate_from_html(html: str, source: str) -> CandidateProfile:
    """Parse candidate data from the provided HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Example parsing logic; these should be replaced with source-specific logic
    name = soup.find("h1").get_text(strip=True)
    photo = soup.find("img", {"class": "candidate-photo"})["src"]
    party = soup.find("span", {"class": "party"}).get_text(strip=True)

    profile = CandidateProfile(
        name=name,
        photo_url=photo,
        party=party,
        roles=[],
        policies={},
        voting_record={},
        funding_sources=[],
        recent_news=[],
        statements=[],
    )
    return profile

def scrape_candidates(urls: List[str]) -> List[CandidateProfile]:
    """Scrape multiple candidate profiles from given URLs."""
    profiles = []
    for url in urls:
        html = fetch_page(url)
        profile = parse_candidate_from_html(html, url)
        if profile.validate():
            profiles.append(profile)
    return profiles
