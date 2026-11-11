import pytest

from shop.cart import Cart, Item


def test_total():
    cart = Cart()
    cart.add(Item("book", 10.0, 2))
    cart.add(Item("pen", 1.5))
    assert cart.total() == 21.5


def test_add_rejects_zero_quantity():
    with pytest.raises(ValueError):
        Cart().add(Item("book", 10.0, 0))
