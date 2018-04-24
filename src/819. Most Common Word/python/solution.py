import collections


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wordDict = collections.Counter(
            [word.strip("!?',;.") for word in paragraph.lower().split(' ')])
        ans, best = None, 0
        for word in wordDict:
            if wordDict[word] > best and word not in banned:
                ans, best = word, wordDict[word]
        return ans
