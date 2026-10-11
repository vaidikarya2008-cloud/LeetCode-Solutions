class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans=0
        length=len(nums)
        for i in range(len(nums)):
            if ((length)%(i+1))==0:
                ans+=(nums[i]*nums[i])
        return ans