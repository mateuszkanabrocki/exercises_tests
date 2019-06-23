import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


def test():
    pass
    # ... your code


if __name__ == "__main__":
    import timeit

    print(timeit.timeit("test()", setup="from __main__ import test", number=100))
