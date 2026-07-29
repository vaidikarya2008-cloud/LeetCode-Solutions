class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]<k:
                count+=1
            else:
                count+=0
        return count
        