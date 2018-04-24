#!/bin/env bash
QUESTION_NAME=$1
mkdir -p "src/${QUESTION_NAME}/python"
touch "src/${QUESTION_NAME}/python/solution.py"
touch "src/${QUESTION_NAME}/python/solution_test.py"
touch "src/${QUESTION_NAME}/question.md"

cat > "src/${QUESTION_NAME}/question.md" << EOL
# ${QUESTION_NAME}

## Description

## Example
EOL
cat > "src/${QUESTION_NAME}/python/solution_test.py" << EOL
import unittest
from solution import Solution


class TestCast(unittest.TestCase):
    test_input_list = [{
    }]

    def test_soluton(self):
        solution = Solution()
        pass


if __name__ == "__main__":
    unittest.main()
EOL