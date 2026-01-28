import requests
from fake_useragent import UserAgent

def fetch_page(url):
    headers = {"User-Agent": UserAgent().random}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text
