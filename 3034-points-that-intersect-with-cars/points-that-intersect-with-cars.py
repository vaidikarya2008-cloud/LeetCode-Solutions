class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        ans = []

        for car in nums:
            for i in range(car[0], car[1] + 1):
                if i not in ans:
                    ans.append(i)

        return len(ans)