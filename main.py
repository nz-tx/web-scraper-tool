import csv
import re
import time

from playwright.sync_api import sync_playwright

# ============================ CONFIG ============================
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
TITLE_SELECTOR = "h3 a"
PRICE_SELECTOR = ".price_color"
MAX_PAGES = 50            # site ceiling (20 books/page -> 1000 books)
PAGE_DELAY = 0.5          # s between page requests (polite scraping)
OUTPUT_FILE = "books.csv"
HEADLESS = True
# =================================================================


def parse_price(text):
    """Extract a numeric price from text like '\u00a330.50'."""
    match = re.search(r"\d+(?:[.,]\d+)*", text.replace(",", ""))
    return float(match.group()) if match else text.strip()


def scrape_page(page, n):
    page.goto(BASE_URL.format(n), timeout=15000)
    titles = page.locator(TITLE_SELECTOR).all_inner_texts()
    prices = page.locator(PRICE_SELECTOR).all_inner_texts()
    return [{"title": t, "price": parse_price(p)} for t, p in zip(titles, prices)]


def run_scraper():
    collected = []
    browser = None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            page = browser.new_page()

            for n in range(1, MAX_PAGES + 1):
                try:
                    found = scrape_page(page, n)
                except Exception as exc:
                    print(f"[scraper] page {n} failed: {exc}")
                    break

                if not found:
                    print(f"[scraper] no books on page {n} - reached the end.")
                    break

                collected.extend(found)
                print(f"[scraper] page {n}: {len(found)} books ({len(collected)} total)")

                if n < MAX_PAGES:
                    time.sleep(PAGE_DELAY)

    except Exception as exc:
        print(f"[scraper] fatal error: {exc}")
    finally:
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass

    if not collected:
        print("[scraper] nothing was scraped.")
        return

    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Book Title", "Price"])
        writer.writerows((b["title"], b["price"]) for b in collected)

    print(f"[scraper] saved {len(collected)} books to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_scraper()