import sys
print('syspath', sys.path.append('/home/ivan/python-polymorphism/strategy_pattern'))
from tic_tac_toe import TicTacToe


def test_easy_game1():
    game = TicTacToe()
    game.go(1, 1)
    game.go()
    game.go(0, 1)
    game.go()
    is_winner = game.go(2, 1)
    assert is_winner


def test_easy_game2():
    game = TicTacToe()
    game.go(1, 1)
    game.go()
    game.go(1, 2)
    assert not game.go()
    assert not game.go(2, 2)
    is_winner = game.go()
    assert is_winner


def test_easy_game3():
    game = TicTacToe()
    game.go(0, 0)
    game.go()
    assert not game.go(1, 1)
    assert not game.go()
    is_winner = game.go(2, 2)
    assert is_winner


def test_normal_game1():
    game = TicTacToe('normal')
    game.go(0, 2)
    game.go()
    game.go(0, 1)
    assert not game.go()
    assert not game.go(1, 2)
    is_winner = game.go()
    assert is_winner


def test_normal_game2():
    game = TicTacToe('normal')
    game.go()
    game.go(2, 1)
    game.go()
    game.go(1, 0)
    assert not game.go()
    assert not game.go(1, 2)
    is_winner = game.go()
    assert is_winner


def test_normal_game3():
    game = TicTacToe('normal')
    game.go(2, 2)
    game.go()
    assert not game.go(1, 1)
    assert not game.go()
    is_winner = game.go(0, 0)
    assert is_winner
