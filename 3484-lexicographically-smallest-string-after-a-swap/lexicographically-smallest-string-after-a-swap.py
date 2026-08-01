class Solution:
    def getSmallestString(self, s: str) -> str:
        lst = []
        lst = list(s)

        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                if int(s[i]) % 2 == int(s[i+1]) % 2:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    return "".join(lst)

        return s