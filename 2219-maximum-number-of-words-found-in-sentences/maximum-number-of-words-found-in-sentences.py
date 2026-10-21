class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lst = []

        for i in range(len(sentences)):
            count = 0

            for j in range(len(sentences[i])):
                if sentences[i][j] == ' ':
                    count += 1

            lst.append(count + 1)

        return max(lst)