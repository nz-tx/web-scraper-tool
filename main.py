import csv
from playwright.sync_api import sync_playwright

def run_scraper():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("http://books.toscrape.com/")
        
        prices = page.locator(".price_color").all_inner_texts()
        titles = page.locator("h3 a").all_inner_texts()
        
        with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            writer.writerow(["Book Title", "Price"])
            
            for title, price in zip(titles, prices):
                writer.writerow([title, price])
                
        browser.close()

run_scraper()