class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        s = sentence.split(' ')
        for i in range(0, len(s) - 1):
            if s[i][-1] != s[i + 1][0]:
                return False
        return True
