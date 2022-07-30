from typing import List

from bs4 import BeautifulSoup
from bs4.element import Tag

from src.utils import compose


def normalize_price(price_str: str) -> float:
    transformation = compose(
                            str.strip, 
                            lambda x: x.replace(u"\xa0", u""),
                            lambda x: x.replace("zł", ""),
                            lambda x: x.replace(" ", "")
                             )
    return float(transformation(price_str))


class ContentParser:
    def __init__(self, html_text: str = "") -> None:
        self.soup = BeautifulSoup(html_text, "lxml")

        self.products = self.get_products()

    def set_html_text(self, new_html_text: str) -> None:
        self.soup = BeautifulSoup(new_html_text, "lxml")

        self.products = self.get_products()

    def get_products(self) -> List[str]:
        return self.soup.find_all("div", {"class": "product-row"})

    def _get_product_name(self, product: Tag) -> str:
        return product.find("h2").text.strip()

    def _get_product_price(self, product: Tag) -> float:
        price_raw = product.find("div", {"class": "price-normal selenium-price-normal"}).text.strip()
        return normalize_price(price_raw)

    def _get_product_spec(self, product: Tag) -> List[str]:
        spec_list = product.find("div", {"class": "product-attributes"}).find_all("div", {"class": "attributes-row"})
        res = {}
        
        for spec in spec_list:
            att_name = spec.find("span", {"class": "attribute-name"}).text.strip()
            att_value = spec.find("span", {"class": "attribute-value"}).text.strip()
            res[att_name] = att_value

        return res

    def parse_single_product(self, product: Tag) -> dict:
        item = {}

        item["name"] = self._get_product_name(product)
        item["price"] = self._get_product_price(product)
        
        item["spec"] = self._get_product_spec(product)

        return item
