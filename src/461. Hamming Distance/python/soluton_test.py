import unittest

from solution import Solution


class TestCase(unittest.TestCase):
    def test_soluton(self):
        solution = Solution()
        x = 1
        y = 4
        result = solution.hammingDistance(x, y)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
