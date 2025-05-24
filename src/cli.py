"""Command line interface for the candidate information application."""

import argparse
from typing import List

from .scraper import scrape_candidates
from .data_store import load_profiles, save_profiles
from .personalization import match_candidates_by_district, compare_candidates
from .recommendation import recommend_candidates


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Candidate info tool")
    subparsers = parser.add_subparsers(dest="command")

    scrape_cmd = subparsers.add_parser("scrape", help="Scrape candidate data")
    scrape_cmd.add_argument("urls", nargs="+", help="Candidate URLs to scrape")

    list_cmd = subparsers.add_parser("list", help="List saved candidates")

    compare_cmd = subparsers.add_parser("compare", help="Compare two candidates")
    compare_cmd.add_argument("name1", help="First candidate name")
    compare_cmd.add_argument("name2", help="Second candidate name")
    compare_cmd.add_argument("issues", nargs="+", help="Issues to compare")

    rec_cmd = subparsers.add_parser("recommend", help="Recommend candidates")
    rec_cmd.add_argument("district", help="Your district")
    rec_cmd.add_argument("prefs", nargs="*", help="issue=stance pairs")

    args = parser.parse_args(argv)

    if args.command == "scrape":
        profiles = scrape_candidates(args.urls)
        save_profiles(profiles)
        print(f"Saved {len(profiles)} candidate profiles")
    elif args.command == "list":
        profiles = load_profiles()
        for p in profiles:
            print(f"{p.name} ({p.party})")
    elif args.command == "compare":
        profiles = load_profiles()
        c1 = next((p for p in profiles if p.name == args.name1), None)
        c2 = next((p for p in profiles if p.name == args.name2), None)
        if not c1 or not c2:
            print("Candidates not found")
            return
        comparison = compare_candidates(c1, c2, args.issues)
        for issue, result in comparison.items():
            print(f"Issue: {issue}")
            for candidate, stance in result.items():
                print(f"  {candidate}: {stance}")
    elif args.command == "recommend":
        profiles = load_profiles()
        district_profiles = match_candidates_by_district(profiles, args.district)
        prefs = dict(pref.split("=", 1) for pref in args.prefs)
        ranked = recommend_candidates(district_profiles, prefs)
        for c in ranked:
            print(c.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
