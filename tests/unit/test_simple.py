import pytest
import requests


@pytest.mark.slow
def test_func_slow():
    print("slow")


def get(url):
    resp = None
    try:
        resp = requests.get(url)
    except Exception as e:
        pytest.raises(e)
    return resp


def test_get(url):
    resp = get(url)
    assert resp.json()["url"] == url
    assert resp.status_code == 200
