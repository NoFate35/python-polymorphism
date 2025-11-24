from user import User
from guest import Guest
from solution import greet


def test_greet():
    guest = Guest()
    assert greet(guest) == 'Nice to meet you Guest!'

    user1 = User('Petr')
    assert greet(user1) == 'Hello Petr!'

    user2 = User('Anna')
    assert greet(user2) == 'Hello Anna!'

    user3 = User('Guest')
    assert greet(user3) == 'Hello Guest!'
