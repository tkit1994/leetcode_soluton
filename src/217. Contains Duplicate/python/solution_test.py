import unittest
from solution import Solution


class TestCast(unittest.TestCase):
    test_input_list = [{
        "input": {"nums":[1,1,2,3,4,5]},
        "output": True,
    }]

    def test_soluton(self):
        solution = Solution()
        for test_input in self.test_input_list:
            result = solution.containsDuplicate(**test_input['input'])
            self.assertEqual(result, test_input["output"])


if __name__ == "__main__":
    unittest.main()
