import json
import logging

from concurrent.futures import ThreadPoolExecutor

import yaml

from src.core import process_page
from src.scraper import Scraper
from src.parser import ContentParser


with open("config.yaml", "r", encoding="utf-8") as config_stream:
        _CONFIG = yaml.safe_load(config_stream)


logging.basicConfig(format=_CONFIG["settings"]["logging_fmt"],
                    level=logging.INFO)


def run_single(page_num):
    
    scraper = Scraper(_CONFIG["resources"]["web"]["base_url"])
    parser = ContentParser()

    items = process_page(scraper, parser, page_num)
    logging.info(f"page no {page_num} processed")
    return items


def main():  
    pages = _CONFIG["settings"]["num_pages"]

    with ThreadPoolExecutor(max_workers=pages) as executor:
        results = executor.map(run_single, range(1, pages + 1))

    flat_results = []

    for res in results:
        flat_results += res

    filename = _CONFIG["settings"]["save_file_name"]
    logging.info("saving results")
    with open(filename, "w") as fp:
        json.dump(flat_results, fp, indent=4)
    logging.info(f"results saved in {filename}")


if __name__ == "__main__":
    main()