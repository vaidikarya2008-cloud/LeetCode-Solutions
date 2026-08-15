class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        count = 0

        for i in range(len(words) - 1):
            if words[i][-1] == words[i + 1][0]:
                count += 1

        if words[-1][-1] == words[0][0]:
            count += 1

        if count == len(words):
            return True
        else:
            return False