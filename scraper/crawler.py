import json
import time
from scraper.fetcher import fetch_page
from scraper.parser import parse_products

BASE_URL = "https://dir.indiamart.com/impcat/led-lights.html"

all_data = []

for page in range(1, 6):
    url = f"{BASE_URL}?page={page}"
    print(f"Scraping: {url}")

    html = fetch_page(url)
    products = parse_products(html)
    all_data.extend(products)

    time.sleep(3)

with open("data/raw_products.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)
# print(html[:2000])
print(f"Total products scraped: {len(all_data)}")


