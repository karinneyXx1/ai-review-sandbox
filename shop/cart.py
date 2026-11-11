"""Корзина интернет-магазина."""

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:
        if item.quantity <= 0:
            raise ValueError("quantity must be positive")
        self.items.append(item)

    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
