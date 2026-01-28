from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    for item in soup.select("li.temp4-card"):
        name_tag = item.select_one("a.prdtitle")
        price_tag = item.select_one("span.prc")
        unit_tag = item.select_one("span.prcut")
        supplier_tag = item.select_one("a.cncf1")
        location_tag = item.select_one("address span")

        products.append({
            "product_name": name_tag.text.strip() if name_tag else None,
            "price": price_tag.text.strip() if price_tag else None,
            "unit": unit_tag.text.strip() if unit_tag else None,
            "supplier": supplier_tag.text.strip() if supplier_tag else None,
            "location": location_tag.text.strip() if location_tag else None,
        })

    return products
