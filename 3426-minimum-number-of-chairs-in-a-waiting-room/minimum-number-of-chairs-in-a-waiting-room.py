class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        maximum = 0

        for i in range(len(s)):
            if s[i] == 'E':
                count += 1
            else:
                count -= 1

            maximum = max(maximum, count)

        return maximum