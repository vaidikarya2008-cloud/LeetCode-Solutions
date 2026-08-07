class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ind = []
        special = []

        for i in range(len(s)):
            if s[i].isalpha():
                ind.append(i)
                special.append(s[i])

        special.reverse()

        lst = list(s)

        for i in range(len(ind)):
            lst[ind[i]] = special[i]

        return "".join(lst)