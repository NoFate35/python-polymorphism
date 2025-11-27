import sys
sys.path.append('/home/ivan/python-polymorphism/state_pattern')
from errors import TcpConnectionError
from tcp_connection import TcpConnection
import pytest


def test_connect1():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    assert connection.get_current_state() == 'connected'
    connection.write('one')
    connection.write('two')
    connection.disconnect()
    assert connection.get_current_state() == 'disconnected'


def test_connect2():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    with pytest.raises(TcpConnectionError):
        connection.connect()


def test_connect3():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    connection.disconnect()
    with pytest.raises(TcpConnectionError):
        connection.disconnect()


def test_connect4():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    connection.disconnect()
    with pytest.raises(TcpConnectionError):
        connection.write('one')
