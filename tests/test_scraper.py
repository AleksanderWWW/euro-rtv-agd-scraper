import pytest

from requests.exceptions import ConnectionError

from src.scraper import Scraper


def test_scraper_instantiates(config):
    base_url = config["resources"]["web"]["base_url"]

    scraper = Scraper(base_url)

    assert scraper


def test_scraper_creates_correct_url(config, scraper):
    true_url = config["resources"]["web"]["base_url"].format("5")

    assert scraper._create_url(5) == true_url

def test_scraper_fetch_returns_string(scraper):
    data = scraper.fetch_data(5)
    assert isinstance(data, str)


def test_scraper_fetch_raises_valueerror(scraper):
    with pytest.raises(ValueError):
        data = scraper.fetch_data("abc")

    
def test_scraper_fetch_raises_connectionerror(scraper):
    scraper.base_url = "http://some-non-existent-url{}.com"
    with pytest.raises(ConnectionError):
        scraper.fetch_data(5)
