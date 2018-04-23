class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseList = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        lookupMap = {
            chr(i): morseList[i - ord('a')]
            for i in range(ord('a'),
                           ord('z') + 1)
        }
        resultList = ["".join([lookupMap[ch] for ch in word]) for word in words]
        resultSet = set(resultList)
        return len(resultSet)
