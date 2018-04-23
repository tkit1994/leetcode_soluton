import unittest

from soluton import Solution


class TestCast(unittest.TestCase):
    test_input_list = [
        {
            "input": ["gin", "zen", "gig", "msg"],
            "output": 2
        },
    ]

    def test_soluton(self):
        solution = Solution()
        for test_input in self.test_input_list:
            result = solution.uniqueMorseRepresentations(test_input["input"])
            self.assertEqual(result, test_input['output'])


if __name__ == '__main__':
    unittest.main()
