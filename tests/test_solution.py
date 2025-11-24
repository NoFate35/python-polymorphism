from solution import DatabaseConfigLoader
from pathlib import Path
import pytest


@pytest.fixture(scope='module')
def loader():
    path = Path(__file__).parent / 'fixtures'
    loader = DatabaseConfigLoader(path)
    return loader


def test_config_loader(loader):
    expected = {
        'host': 'google.com',
        'username': 'postgres',
    }
    assert loader.load('production') == expected


def test_config_loader2(loader):
    expected = {
      'username': 'mysupername',
    }
    assert loader.load('custom') == expected


def test_config_loader3(loader):
    expected = {
      'host': 'localhost',
      'username': 'postgres',
      'port': 5000,
    }
    assert loader.load('development') == expected


def test_config_loader4(loader):
    expected = {
      'host': 'dev.server',
      'username': 'postgres',
      'port': 5000,
      'password': 'admin',
    }
    assert loader.load('preproduction') == expected
