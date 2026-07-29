class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        count1 = 0

        for i in range(len(nums)):
            count += nums[i]
            if count == 0:
                count1 += 1

        return count1