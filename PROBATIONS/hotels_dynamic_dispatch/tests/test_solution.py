import sys
sys.path.append('/home/ivan/python-polymorphism/PROBATIONS/hotels_dynamic_dispatch')
sys.path.append('/data/data/com.termux/files/home/python-polymorphism/PROBATIONS/hotels_dynamic_dispatch')
from solution import find_the_cheapest_service
import json
import pytest
import pathlib


@pytest.fixture()
def data():
    with open(pathlib.Path(__file__).parent / 'data.json') as f:
        return json.loads(f.read())


def test_with_min_max(data):
    expected = {
        'hotel': {'cost': 616, 'name': 'python_inn'},
        'service': 'kostrovok'
        }
    predicates = {'min': 600, 'max': 800}
    result = find_the_cheapest_service(data, predicates)
    assert result == expected

    expected2 = {
        'hotel': {'cost': 672, 'name': '$phpInn'},
        'service': 'kostrovok'
        }
    predicates2 = {'min': 650, 'max': 700}
    result2 = find_the_cheapest_service(data, predicates2)
    assert result2 == expected2


def test_with_only_min(data):
    expected = {
        'hotel': {'cost': 802.5, 'name': 'JavaInn'},
        'service': 'book-king'
        }
    predicates = {'min': 800}
    result = find_the_cheapest_service(data, predicates)
    assert result == expected


def test_with_only_max(data):
    expected = {
        'hotel': {'cost': 500, 'name': 'python_inn'},
        'service': 'airdnb'
        }
    predicates = {'max': 570}
    result = find_the_cheapest_service(data, predicates)
    assert result == expected


def test_with_nothing(data):
    expected = {
        'hotel': {'cost': 500, 'name': 'python_inn'},
        'service': 'airdnb'
        }
    result = find_the_cheapest_service(data)
    assert result == expected
