from src.parser import ContentParser
from src.core import process_page


def test_returned_list_has_items(scraper):
    parser = ContentParser()

    items = process_page(scraper, parser, page_num=1)

    assert items


def test_process_page_returns_list_of_dicts(scraper):
    parser = ContentParser()

    items = process_page(scraper, parser, page_num=1)

    for item in items:
        assert isinstance(item, dict)


def test_process_page_dicts_have_correct_keys(scraper):
    parser = ContentParser()

    items = process_page(scraper, parser, page_num=1)

    for item in items:
        for key in ['name', 'price', 'spec']:
            assert key in item