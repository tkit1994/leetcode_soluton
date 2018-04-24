import unittest
from solution import Solution


class TestCast(unittest.TestCase):
    test_input_list = [{
        "input": {
            "paragraph":
            "Bob hit a ball, the hit BALL flew far after it was hit.",
            "banned": ["hit"],
        },
        "output": "ball",
    }]

    def test_soluton(self):
        solution = Solution()
        for test_input in self.test_input_list:
            result = solution.mostCommonWord(**test_input["input"])
            self.assertEqual(result, test_input["output"])


if __name__ == "__main__":
    unittest.main()
