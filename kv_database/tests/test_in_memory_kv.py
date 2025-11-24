import copy
from kv_database.in_memory_kv import InMemoryKV


def test_in_memory_kv():
    data = {'key': 10}
    map = InMemoryKV(data)

    assert map.get_('key2') is None
    assert map.get_('key2', 'default') == 'default'
    assert map.get_('key') == 10
    assert map.get_('key', 'default') == 10

    map.set_('key2', 'value2')
    map.set_('key', 'value')

    assert map.get_('key2', 'default') == 'value2'
    assert map.get_('key2') == 'value2'
    assert map.get_('key') == 'value'

    map.unset_('key')

    assert map.get_('key') is None
    assert map.to_dict() == {'key2': 'value2'}


def test_get_default_value():
    data = {'key': 10}
    map = InMemoryKV(data)

    assert map.get_('key2', 'default') == 'default'

    map.set_('key2', False)
    assert map.get_('key2', 'default') is False


def test_must_be_immutable():
    data = {'key': 10}
    data_copy = copy.deepcopy(data)
    map = InMemoryKV(data)

    data['key2'] = 'value2'
    assert map.to_dict() == data_copy

    map2 = map.to_dict()
    map2['key2'] = 'value2'
    assert map.to_dict() == data_copy


def test_deep_immutable():
    data = {'key1': 'value1', 'key2': {'key3': 'value2'}}
    data_copy = copy.deepcopy(data)
    map = InMemoryKV(data)

    map2 = map.to_dict()
    map2['key2']['key3'] = 'another value'

    assert map.to_dict() == data_copy
