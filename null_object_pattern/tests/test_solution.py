from user import User
from subscription import Subscription


def test_subscription():
    user = User('vasya@email.com', Subscription('premium'))
    assert user.get_current_subscription().has_premium_access()
    assert not user.get_current_subscription().has_professional_access()


def test_subscription_2():
    user = User('vasya@email.com', Subscription('professional'))
    assert not user.get_current_subscription().has_premium_access()
    assert user.get_current_subscription().has_professional_access()


def test_subscription_3():
    user = User('vasya@email.com')
    assert not user.get_current_subscription().has_premium_access()
    assert not user.get_current_subscription().has_professional_access()


def test_subscription_4():
    user = User('rakhim@hexlet.io')  # администратор, проверяется по емейлу
    assert user.get_current_subscription().has_premium_access()
    assert user.get_current_subscription().has_professional_access()
