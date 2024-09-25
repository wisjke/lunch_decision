import json
from datetime import date
from typing import Iterable

import requests


def test_menu_get():
    res = requests.get(r"http://127.0.0.1:8000/api/menus")
    assert res.status_code == 200


def test_menu_is_list():
    res = requests.get(r"http://127.0.0.1:8000/api/menus")
    assert type(res.json()) == list


def test_menu_content():
    res = requests.get(r"http://127.0.0.1:8000/api/menus")
    menus = res.json()
    if menus:
        assert 'id' in menus[0]
        assert 'restaurant' in menus[0]
        assert 'day' in menus[0]
        assert 'items' in menus[0]



