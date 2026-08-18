class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)):
            j = len(s) - 1 - i

            if i < j:
                s[i], s[j] = s[j], s[i]