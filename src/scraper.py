import logging

import requests
from requests.exceptions import HTTPError


class Scraper:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def _create_url(self, page_num: int) -> str:
        return self.base_url.format(str(page_num))

    def fetch_data(self, page_num: int) -> str:
        page_num = int(page_num)

        logging.info(f"fetching page no {page_num}")

        url = self._create_url(page_num)
        resp = requests.get(url)

        if resp.ok:
            logging.info(f"page no {page_num} fetched")
            return resp.text
        
        logging.error(f"page no {page_num} returned invalid status code: {resp.status_code}")
        raise HTTPError(f"Request returned response with status code: {resp.status_code}")
