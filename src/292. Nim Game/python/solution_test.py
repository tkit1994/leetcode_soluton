import unittest
from solution import Solution


class TestCast(unittest.TestCase):
    test_input_list = [{
        "input": {"n": 1},
        "output": True,
    }]

    def test_soluton(self):
        solution = Solution()
        for test_input in self.test_input_list:
            result = solution.canWinNim(**test_input["input"])
            self.assertEqual(test_input['output'], result)


if __name__ == "__main__":
    unittest.main()
