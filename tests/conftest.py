import yaml
import pytest

from src.scraper import Scraper
from src.parser import ContentParser


@pytest.fixture(scope="session")
def config() -> dict:
    with open("config.yaml", "r", encoding="utf-8") as config_stream:
        config = yaml.safe_load(config_stream)

    return config


@pytest.fixture(scope="session")
def scraper() -> Scraper:
    with open("config.yaml", "r", encoding="utf-8") as config_stream:
        config_dict = yaml.safe_load(config_stream)
    return Scraper(config_dict["resources"]["web"]["base_url"])


@pytest.fixture(scope="session")
def sample_html() -> str:
    with open("sample_html.txt", "r", encoding="utf-8") as fp:
        return fp.read()

    
# @pytest.fixture(scope="session")
# def parser() -> ContentParser:
#     with open("sample_html.txt", "r", encoding="utf-8") as fp:
#         html = fp.read()

#     return ContentParser(html)
    