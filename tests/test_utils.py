# flake8: noqa

from lyrics import utils


def test_safe_filename():
    assert utils.safe_filename("What's the matter", ".json") == "what-s_the_matter.json"


def test_url_data():
    url_data = utils.UrlData("https://www.google.com")
    assert url_data.bs
    assert url_data._html
    assert url_data._resp
    assert url_data._bs