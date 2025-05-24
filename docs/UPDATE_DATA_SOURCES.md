# Updating Data Sources

The scraper relies on parsing specific websites. To add new data sources or adapt to new regions:

1. Identify official candidate pages, campaign finance sites, and reputable news sources for the region.
2. Update `src/scraper.py` with new parsing logic in `parse_candidate_from_html`.
3. Validate that the parsed data includes required fields (`name`, `party`).
4. Run `python -m src.cli scrape <new_urls>` to refresh stored profiles.

For new election cycles, adjust the URLs and district-matching logic in `src/personalization.py` to recognize updated districts and offices.
