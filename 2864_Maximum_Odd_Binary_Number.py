# LeetCode 2864
# Maximum Odd Binary Number
# Difficulty: Easy

class Solution:
    ...class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        lst = list(map(int, s))
        count1 = 0
        count0 = 0

        for i in range(len(lst)):
            if lst[i] == 1:
                count1 += 1
            else:
                count0 += 1

        reduc = count1 - 1

        return "1" * reduc + "0" * count0 + "1"
