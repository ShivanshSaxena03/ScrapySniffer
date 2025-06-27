# ScrapySniffer
📰 Python web scraper for Hacker News. Fetches top stories from multiple pages, filters by votes, and sorts by popularity.

# Hacker News Scraper 🕵️‍♂️

A Python web scraper that fetches and ranks the top stories from [Hacker News](https://news.ycombinator.com/) based on vote count.

## 🔍 Features

- Scrapes titles and URLs from the first two pages of Hacker News.
- Filters stories with more than 99 points.
- Sorts them in ascending order by vote count.
- Displays results in a clean format using `pprint`.

## 🧰 Requirements

- Python 3
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
RUN:
python scraper.py

🧠 How It Works
Sends HTTP requests to the first two pages of Hacker News.

Parses HTML using BeautifulSoup.

Extracts:

Titles and links from .titleline a

Vote counts from .subtext .score

Filters posts with >99 points.

Sorts and displays using pprint.
