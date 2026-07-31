class Solution:
    def clearDigits(self, s: str) -> str:
        lst = []

        for i in range(len(s)):
            if s[i].isalpha():
                lst.append(s[i])
            else:
                lst.pop()

        return "".join(lst)