import sys
sys.path.append('/home/ivan/python-polymorphism/factory_pattern')
from pathlib import Path
from config_factory import ConfigFactory


def fixture_path(filename):
    return Path(__file__).parent / 'fixtures' / filename


def test_yml():
    config = ConfigFactory.factory(fixture_path('test.yml'))
    assert config.get_value('key') == 'value'


def test_yaml():
    config = ConfigFactory.factory(fixture_path('test2.yaml'))
    assert config.get_value('key') == 'another value'


def test_json():
    config = ConfigFactory.factory(fixture_path('test.json'))
    assert config.get_value('key') == 'something else'


def test_json2():
    config = ConfigFactory.factory(fixture_path('test2.json'))
    assert config.get_value('files').get_value('config') == 'json'
