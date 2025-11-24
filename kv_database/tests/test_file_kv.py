import json
import pytest
from kv_database.file_kv import FileKV


@pytest.fixture
def json_data(tmp_path):
    filepath = tmp_path / "data.json"
    with open(filepath, 'w+') as f:
        f.write(json.dumps({}))
    return filepath


def test_file_kv(json_data):
    map = FileKV(json_data)

    map.set_('key', 10)

    assert map.get_('key2') is None
    assert map.get_('key2', 'default') == 'default'
    assert map.get_('key') == 10
    assert map.get_('key', 'default') == 10

    map.set_('key2', 'value2')
    map.set_('key', 'value')

    assert map.get_('key2') == 'value2'
    assert map.get_('key2', 'default') == 'value2'
    assert map.get_('key') == 'value'

    map.unset_('key')

    assert map.get_('key') is None
    assert map.to_dict() == {'key2': 'value2'}


def test_get_default_value(json_data):
    map = FileKV(json_data)

    map.set_('key', 10)
    assert map.get_('key2', 'default') == 'default'

    map.set_('key2', False)
    assert map.get_('key2', 'default2') is False
