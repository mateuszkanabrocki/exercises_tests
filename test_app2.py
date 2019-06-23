# import pytest


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"


if __name__ == "__main__":
    # we do not run it via pytest, but some builtin testing framework
    test_sum()
    test_sum_tuple()
    print("Everything passed")
