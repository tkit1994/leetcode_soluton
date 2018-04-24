import unittest
from solution import Solution


class TestCast(unittest.TestCase):
    test_input_list = [{
        'input': {
            "nums": [2, 7, 11, 15],
            "target": 9
        },
        'output': [0, 1]
    }]

    def test_soluton(self):
        solution = Solution()
        for test_input in self.test_input_list:
            result = solution.twoSum(**test_input['input'])
            self.assertEqual(result, test_input['output'])


if __name__ == "__main__":
    unittest.main()