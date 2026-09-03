# Web Scraper & Automation Tool

A Python-based automation and data extraction utility built using Playwright. It automatically navigates through web pages, extracts structured textual data (such as product titles and prices), and exports the results directly into a clean CSV file.

## Features
- Automated browser control with Playwright (Chromium).
- Extracts specific data points using robust CSS selectors.
- Automatically handles file I/O to export data into organized CSV format.
- Lightweight and easy to configure for various web targets.

## Technologies Used
- Python 3.11
- Playwright for Python
- Built-in CSV module

## Usage
1. Install dependencies: `pip install playwright` then `playwright install`
2. Run the script: `python main.py`
3. The extracted data will be automatically saved as `books.csv` in the project directory.