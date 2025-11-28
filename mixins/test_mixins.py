from mixins import EqualityMixin, SerializeMixin
from classes import User as BaseUser, ShoppingCart as BaseCart


def test_equality_mixin():
    class User(BaseUser, EqualityMixin):
        pass

    user1 = User('John', 'john@mail.com', 'password')
    user2 = User('John', 'john@mail.com', 'password')
    user3 = User('Alice', 'alice@mail.com', 'password')

    assert user1 == user2
    assert user1 != user3

    class Cart(BaseCart, EqualityMixin):
        pass

    cart1 = Cart(['cat', 'dog'])
    cart2 = Cart(['cat'])
    cart3 = Cart(['cat', 'cat', 'dog'])
    cart2.add_item('dog')

    assert cart1 == cart2
    assert cart1 != cart3

    user4 = BaseUser('John', 'john@mail.com', 'password')
    assert user1 != user4, 'Mixin should compare same class'


def test_serialize_mixin():
    class Cart(BaseCart, EqualityMixin, SerializeMixin):
        pass

    cart1 = Cart(['cat', 'dog'])
    data1 = cart1.serialize()

    cart2 = Cart.deserialize(data1)
    assert cart1 == cart2, 'EqualityMixin should work'
    assert cart1 is not cart2, 'SerializeMixin should return new object'
