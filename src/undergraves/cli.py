import sys
from urllib.parse import urlparse
from undergraves.crawler import crawl
from undergraves.exporter import save_to_json, save_to_csv

VALID_LEVELS = ["T1", "T2", "T3", "T4", "T5"]

def is_valid_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return bool(parsed.netloc and parsed.scheme in ["http", "https"])
    except Exception:
        return False

def run():
    if len(sys.argv) < 2:
        print("Usage: undergraves <URL> [LEVEL]")
        print("Example: undergraves https://example.com T2")
        sys.exit(1)

    target_url = sys.argv[1]

    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "https://" + target_url

    if not is_valid_url(target_url):
        print(f"[-] Invalid URL: {target_url}")
        sys.exit(1)

    user_level = "T3"

    if len(sys.argv) > 2:
        provided_level = sys.argv[2].upper()
        if provided_level not in VALID_LEVELS:
            print(f"[-] Invalid scan level: {sys.argv[2]}. Allowed: {', '.join(VALID_LEVELS)}")
            sys.exit(1)
        user_level = provided_level

    print(f"[*] Starting Undergraves scan against {target_url} (Level {user_level})")

    try:
        pages = crawl(target_url, level=user_level)

        if not pages:
            print("[-] No targets mapped or host unreachable.")
            sys.exit(0)

        save_to_json(pages, "resultado.json")
        save_to_csv(pages, "resultado.csv")

        print(f"[+] Scan completed. {len(pages)} endpoints mapped.")
        print("[+] Results saved to 'resultado.json' and 'resultado.csv'.")

    except KeyboardInterrupt:
        print("\n[-] Scan aborted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[-] Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()