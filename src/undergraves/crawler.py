import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

SCAN_LEVELS = {
    "T1": 50,
    "T2": 200,
    "T3": 500,
    "T4": 2000,
    "T5": None
}

def crawl(url: str, level: str = "T3") -> list:
    max_pages = SCAN_LEVELS.get(level.upper(), 500)

    visited = set()
    to_visit = [url]
    results = []
    
    domain_parse = urlparse(url).netloc

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    while to_visit:
        if max_pages is not None and len(visited) >= max_pages:
            break

        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        try:
            response = requests.get(current_url, headers=headers, timeout=5)
            
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            
        except Exception:
            continue

        visited.add(current_url)

        title_text = soup.title.string.strip() if soup.title and soup.title.string else "N/A"

        print(f"[200] {current_url} | Title: {title_text}")

        results.append({
            "url": current_url,
            "title": title_text
        })

        for link in soup.find_all("a"):
            href = link.get("href")

            if not href:
                continue

            href = urljoin(current_url, href)
            href_parse = urlparse(href).netloc

            if href_parse == domain_parse and href not in visited and href not in to_visit:
                to_visit.append(href)

    return results