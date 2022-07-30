from typing import List


def process_page(scraper, parser, page_num: int) -> List[dict]:
    result = []

    html_text = scraper.fetch_data(page_num)
    parser.set_html_text(html_text)

    for product in parser.products:
        result.append(parser.parse_single_product(product))

    return result
