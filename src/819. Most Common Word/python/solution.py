import collections


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wordList = [
            word.strip("!?',;.") for word in paragraph.lower().split(' ')
        ]
        wordCounter = collections.Counter(filter(lambda x: x not in banned, wordList))
        return wordCounter.most_common()[0][0]
