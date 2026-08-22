class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        lst = list(map(int, str(num)))

        while len(lst) > 1:
            sum = 0

            for i in range(len(lst)):
                sum += lst[i]

            lst = list(map(int, str(sum)))

        return lst[0]