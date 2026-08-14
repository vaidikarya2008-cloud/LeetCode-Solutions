class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            left = 0
            for j in range(i):
                left += nums[j]
            right = 0
            for j in range(i + 1, len(nums)):
                right += nums[j]
            ans.append(abs(left-right))
        return ans