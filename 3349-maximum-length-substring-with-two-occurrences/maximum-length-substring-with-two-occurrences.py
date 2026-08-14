class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        lst = []
        ans = 0

        for i in range(len(s)):
            while lst.count(s[i]) >= 2:
                lst.pop(0)

            lst.append(s[i])

            ans = max(ans, len(lst))

        return ans