import sys
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def validate_url(url: str) -> bool:
    """Check if the URL looks valid."""
    parsed = urlparse(url)
    return parsed.scheme in ["http", "https"] and bool(parsed.netloc)


def fetch_html(url: str) -> str:
    """Fetch raw HTML from a website."""
    if not validate_url(url):
        raise ValueError("Invalid URL. Please include http:// or https://")

    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return response.text


def extract_text_from_html(html: str) -> str:
    """Extract clean readable text from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    lines = []
    for line in text.splitlines():
        cleaned = line.strip()
        if cleaned:
            lines.append(cleaned)

    return "\n".join(lines)


def scrape_website(url: str) -> str:
    """Fetch a website and return clean text."""
    html = fetch_html(url)
    text = extract_text_from_html(html)
    return text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.scraper https://example.com")
        sys.exit(1)

    website_url = sys.argv[1]
    extracted_text = scrape_website(website_url)

    print(extracted_text[:2000])