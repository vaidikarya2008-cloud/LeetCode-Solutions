class Solution:

    def countSymmetricIntegers(self, low: int, high: int) -> int:

        lst = []

        ans = 0

        count = 0

        for i in range(low, high + 1):

            lst = list(map(int, str(i)))

            if len(lst) % 2 != 0:
                continue

            first = sum(lst[:len(lst)//2])
            second = sum(lst[len(lst)//2:])

            if first == second:
                ans += 1

            lst = []

        return ans