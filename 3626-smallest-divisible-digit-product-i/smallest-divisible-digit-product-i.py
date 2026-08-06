class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            lst = [int(i) for i in str(n)]
            pro = 1

            for x in lst:
                pro *= x

            if pro % t == 0:
                return n

            n += 1