import pytest
from chain import chain


def test_chain_with_multiple_iterables():
    result = list(chain([1, 2, 3], ["a", "b"], (True, False)))
    assert result == [1, 2, 3, "a", "b", True, False]


def test_chain_with_single_iterable():
    result = list(chain([1, 2, 3]))
    assert result == [1, 2, 3]


def test_chain_with_empty_iterables():
    result = list(chain([], (), []))
    assert result == []


def test_chain_with_mixed_types():
    result = list(chain("abc", [1, 2, 3], (4.5, 6.7)))
    assert result == ["a", "b", "c", 1, 2, 3, 4.5, 6.7]


def test_chain_with_nested_iterables():
    result = list(chain([[1, 2], [3, 4]], [(5, 6)]))
    print(result)
    assert result == [[1, 2], [3, 4], (5, 6)] 


def test_chain_with_large_input():
    large_iterable = range(1000)
    result = list(chain(large_iterable))
    assert result == list(range(1000))


def test_chain_with_no_arguments():
    result = list(chain())
    assert result == []


def test_chain_generator_as_input():
    def generator():
        yield from range(3)

    result = list(chain(generator(), [3, 4]))
    assert result == [0, 1, 2, 3, 4]
