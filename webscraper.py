import requests
from bs4 import BeautifulSoup
import csv
import sys
from urllib.parse import urljoin, urlparse


BAD_PATTERNS = [
    "login", "signup", "register", "mailto:",
    "javascript:", "#"
]


def fetch_page(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    return response.text


def is_valid_link(link: str):
    if not link:
        return False

    for pattern in BAD_PATTERNS:
        if pattern in link.lower():
            return False

    return True


def extract_summary(container):
    # пытаемся найти краткое описание рядом со статьей
    p = container.find("p")

    if p:
        text = p.get_text(strip=True)
        if len(text) > 30:
            return text[:200]

    return "N/A"


def extract_items(html: str, base_url: str):
    soup = BeautifulSoup(html, "html.parser")

    items = []
    seen = set()

    containers = soup.find_all(["article", "div", "section"])

    for c in containers:
        title_tag = c.find(["h1", "h2", "h3"])

        if not title_tag:
            continue

        link_tag = title_tag.find("a")

        if not link_tag:
            continue

        href = link_tag.get("href")

        if not is_valid_link(href):
            continue

        full_url = urljoin(base_url, href)

        if full_url in seen:
            continue

        seen.add(full_url)

        title = title_tag.get_text(strip=True)

        summary = extract_summary(c)

        items.append({
            "title": title,
            "url": full_url,
            "summary": summary
        })

    return items


def save_csv(data, filename="linux.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "url", "summary"]
        )

        writer.writeheader()
        writer.writerows(data)


def main():
    if len(sys.argv) < 2:
        print("usage: python webscraper.py <url>")
        return

    url = sys.argv[1]

    html = fetch_page(url)

    items = extract_items(html, url)

    save_csv(items)

    print(f"saved {len(items)} rows")


if __name__ == "__main__":
    main()