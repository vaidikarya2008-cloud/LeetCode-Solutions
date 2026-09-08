class Solution:
    def countCommas(self, n: int) -> int:

        first = 0
        second = 0
        third = 0

        for i in range(1, n + 1):

            if i < 1000:
                first += 0

            elif i < 1000000:
                second += 1

            else:
                third += 2

        return first + second + third