import sys
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


RELEVANT_KEYWORDS = [
    "about",
    "company",
    "services",
    "solutions",
    "products",
    "platform",
    "customers",
    "careers",
    "team",
    "contact",
    "pricing",
    "industries",
]


SKIP_KEYWORDS = [
    "privacy",
    "terms",
    "cookie",
    "login",
    "signin",
    "sign-in",
    "signup",
    "sign-up",
    "blog",
    "news",
    "press",
    "facebook",
    "twitter",
    "x.com",
    "linkedin",
    "instagram",
    "youtube",
]


def validate_url(url: str) -> bool:
    """Check if the URL looks valid."""
    parsed = urlparse(url)
    return parsed.scheme in ["http", "https"] and bool(parsed.netloc)


def clean_url(url: str) -> str:
    """Remove fragments and query parameters from a URL."""
    parsed = urlparse(url)
    cleaned = parsed._replace(query="", fragment="")
    return urlunparse(cleaned)


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


def is_same_domain(base_url: str, candidate_url: str) -> bool:
    """Check whether a link belongs to the same website."""
    base_domain = urlparse(base_url).netloc.replace("www.", "")
    candidate_domain = urlparse(candidate_url).netloc.replace("www.", "")
    return base_domain == candidate_domain


def is_relevant_link(url: str) -> bool:
    """Check whether a link looks useful for brochure generation."""
    lower_url = url.lower()

    if any(skip_word in lower_url for skip_word in SKIP_KEYWORDS):
        return False

    return any(keyword in lower_url for keyword in RELEVANT_KEYWORDS)


def extract_relevant_links(html: str, base_url: str, max_links: int = 5) -> list[str]:
    """Find useful internal links from a company homepage."""
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for anchor in soup.find_all("a", href=True):
        href = anchor["href"]
        full_url = clean_url(urljoin(base_url, href))

        if not validate_url(full_url):
            continue

        if not is_same_domain(base_url, full_url):
            continue

        if not is_relevant_link(full_url):
            continue

        if full_url not in links:
            links.append(full_url)

    return links[:max_links]


def scrape_website(url: str) -> str:
    """
    Scrape a company website.

    This function starts with the homepage, finds useful internal links,
    scrapes those pages, and combines the content.
    """
    homepage_html = fetch_html(url)
    homepage_text = extract_text_from_html(homepage_html)

    relevant_links = extract_relevant_links(homepage_html, url)

    all_content = [
        f"Source: {url}",
        homepage_text,
    ]

    for link in relevant_links:
        try:
            page_html = fetch_html(link)
            page_text = extract_text_from_html(page_html)

            all_content.append("\n\n---\n")
            all_content.append(f"Source: {link}")
            all_content.append(page_text)

        except Exception as error:
            all_content.append(f"\n\nCould not scrape {link}: {error}")

    return "\n".join(all_content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.scraper https://example.com")
        sys.exit(1)

    website_url = sys.argv[1]
    extracted_text = scrape_website(website_url)

    print(extracted_text[:4000])