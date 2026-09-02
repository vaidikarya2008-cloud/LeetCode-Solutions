class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()

        for i in range(len(nums)):
            ans.add(nums[i])
            ans.add(int(str(nums[i])[::-1]))

        return len(ans)