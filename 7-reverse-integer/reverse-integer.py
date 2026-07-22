class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        nx = -1 * x
        nstring = str(nx)
        list1 = []

        if x > 0:
            for i in range(-1, -len(string)-1, -1):
                list1.append(string[i])

            ans = int(''.join(map(str, list1)))

            if ans > 2147483647:
                return 0

            return ans

        else:
            for i in range(-1, -len(nstring)-1, -1):
                list1.append(string[i])

            ans = -int(''.join(map(str, list1)))

            if ans < -2147483648:
                return 0

            return ans