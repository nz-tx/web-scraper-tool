# Web Scraper & Automation Tool

A Python-based automation and data extraction utility built using Playwright. It navigates through an entire online catalog page by page, extracts structured data (product titles and prices), and exports the results into a clean CSV file.

## Features
- Automated browser control with Playwright (Chromium).
- Extracts data using configurable CSS selectors.
- **Full catalog pagination**: iterates every page of the site until no more books exist (default ceiling 50 pages / 1000 books).
- **Polite scraping**: configurable delay between page requests.
- **Price normalization**: `£30.50` is parsed and exported as a numeric value.
- Robust error handling: page failures and browser errors are reported and resources are always released.
- Exports to UTF-8 CSV.

## Technologies Used
- Python 3.11
- Playwright for Python
- Built-in CSV module

## Setup
```bash
pip install -r requirements.txt
playwright install chromium
```

## Usage
```bash
python main.py
```
Run the script, and the extracted data will be saved as `books.csv` in the project directory.

## Configuration
Tune behavior at the top of `main.py`:

| Constant         | Default                               | Meaning                            |
| ---------------- | -------------------------------------- | ----------------------------------- |
| `BASE_URL`       | `http://books.toscrape.com/catalogue/page-{}.html` | Page template with `{}` as page number |
| `TITLE_SELECTOR` | `h3 a`                                 | CSS selector for titles            |
| `PRICE_SELECTOR` | `.price_color`                         | CSS selector for prices            |
| `MAX_PAGES`      | `50`                                   | Maximum pages to scrape            |
| `PAGE_DELAY`     | `0.5`                                  | Seconds between page requests      |
| `OUTPUT_FILE`    | `books.csv`                            | Output CSV filename                |
| `HEADLESS`       | `True`                                 | Run the browser without a window   |

To target a different site, update `BASE_URL` plus the two selectors.