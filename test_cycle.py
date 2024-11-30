import pytest
from cycle import cycle, take


def test_cycle_with_list():
    iterable = [1, 2, 3]
    result = take(cycle(iterable), 10)
    assert result == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]


def test_cycle_with_tuple():
    iterable = (4, 5)
    result = take(cycle(iterable), 6)
    assert result == [4, 5, 4, 5, 4, 5]


def test_cycle_with_string():
    iterable = "AB"
    result = take(cycle(iterable), 5)
    assert result == ["A", "B", "A", "B", "A"]


def test_cycle_with_empty_iterable():
    iterable = []
    result = next(cycle(iterable))
    assert result == None

def test_take_with_zero_quantity():
    iterable = [1, 2, 3]
    result = take(cycle(iterable), 0)
    assert result == []


def test_take_with_negative_quantity():
    iterable = [1, 2, 3]
    result = take(cycle(iterable), -5)
    assert result == []
