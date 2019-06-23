import pytest


def test_app():
    assert sum([1, 2, 3]) == 6
    sum1 = sum([1, 2, 3])
    assert sum1 == 5, "Should be 6"
    assert sum([1, 2, 3]) == 5, "Should be 6"


if __name__ == '__main__':
    pytest.main()