from kv_database.in_memory_kv import InMemoryKV
from kv_database.solution import swap_key_value


def test_swap_key_value():
    map = InMemoryKV({'key': 10})
    map.set_('key2', 'value2')
    swap_key_value(map)

    assert map.get_('key') is None
    assert map.get_(10) == 'key'
    assert map.get_('value2') == 'key2'


def test_swap_key_value2():
    map = InMemoryKV({'foo': 'bar', 'bar': 'zoo'})

    swap_key_value(map)
    assert map.to_dict() == {'bar': 'foo', 'zoo': 'bar'}
