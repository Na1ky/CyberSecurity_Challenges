# Te.sts for the api. module
from src.api import BASE_URL


def test_base_url():
    # The url should always use ht.tps
    assert BASE_URL.startswith("https://")
