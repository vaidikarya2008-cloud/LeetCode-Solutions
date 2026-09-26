class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []

        ans = []
        k = 0

        for i in range(m):
            lst = []
            for j in range(n):
                lst.append(original[k])
                k += 1
            ans.append(lst)

        return ans