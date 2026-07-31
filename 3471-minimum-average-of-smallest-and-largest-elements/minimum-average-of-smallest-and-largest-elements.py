class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        small=[]
        nums.sort()
        for i in range(len(nums)//2):
            small.append((nums[0]+nums[-1])/2)
            nums.pop(0)
            nums.pop()
        return min(small)
