class Solution:
    def smallestNumber(self, n: int) -> int:
        s = bin(n)[2:]

        while '0' in s:
            n = n + 1
            s = bin(n)[2:]

        return n