class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        ans = 0

        for i in range(len(nums)):
            start = i - nums[i]

            if start < 0:
                start = 0

            for j in range(start, i + 1):
                ans += nums[j]

        return ans