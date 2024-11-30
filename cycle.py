from collections.abc import Iterable


def cycle(iterable: Iterable):
    while True:
        if not iterable:
            yield None
        for item in iterable:
            yield item


def take(iterable: Iterable, quantity: int):
    return [next(iterable) for _ in range(quantity)]
