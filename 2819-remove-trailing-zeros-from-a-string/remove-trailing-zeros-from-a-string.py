class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans = list(num)

        for i in range(len(ans)):
            if ans[-1] == '0':
                ans.pop()
            else:
                break

        return "".join(ans)