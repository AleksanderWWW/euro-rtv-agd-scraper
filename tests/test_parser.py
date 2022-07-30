from src.parser import ContentParser, normalize_price


def test_normalize_price():
    res = normalize_price('4\xa0399\xa0zł')
    assert res == 4399

def test_content_parser_instantiates():
    html_text = ""
    ContentParser(html_text)
    assert True


def test_html_tag_in_soup(sample_html):
    parser = ContentParser(sample_html)
    assert parser.soup.find('html')


def test_parser_products_list_length(sample_html):
    parser = ContentParser(sample_html)
    assert len(parser.products) == 28


def test_get_name(sample_html):
    parser = ContentParser(sample_html)
    product = parser.products[0]

    assert "Laptop ASUS TUF Gaming F15 FX506HEB-HN188W" in parser._get_product_name(product)


def test_get_price(sample_html):
    parser = ContentParser(sample_html)
    product = parser.products[0]

    assert parser._get_product_price(product) == 4_399


def test_get_spec(sample_html):
    parser = ContentParser(sample_html)
    product = parser.products[0]

    assert parser._get_product_spec(product) == {
        'Ekran': '15,6 cala,  1920 x 1080 pikseli 144 Hz', 
        'Procesor': 'Intel® Core™ i5 11gen 11400H 2,7 - 4,5 GHz', 
        'Pamięć': '16 GB  DDR4 3200 MHz RAM', 
        'Grafika': 'NVIDIA® GeForce RTX™ 3050 Ti + Intel UHD Graphics', 
        'Dysk': '512 GB SSD', 
        'System operacyjny': 'Windows 11 Home Edition'
        }


def test_parse_single_product(sample_html):
    parser = ContentParser(sample_html)
    product = parser.products[0]

    item = parser.parse_single_product(product)

    for key in ['name', 'price', 'spec']:
        assert key in item
