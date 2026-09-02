class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()

        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.add(nums[i])

        for i in range(len(nums)):
            r = int(str(nums[i])[::-1])

            if r not in ans:
                ans.add(r)

        return len(ans)