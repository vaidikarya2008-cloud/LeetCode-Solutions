class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst1 = list(word1)
        lst2 = list(word2)
        lst3 = []

        m = min(len(lst1), len(lst2))

        for i in range(m):
            lst3.append(lst1[i])
            lst3.append(lst2[i])

        if len(lst1) > len(lst2):
            lst3.extend(lst1[m:])
        else:
            lst3.extend(lst2[m:])

        return "".join(lst3)