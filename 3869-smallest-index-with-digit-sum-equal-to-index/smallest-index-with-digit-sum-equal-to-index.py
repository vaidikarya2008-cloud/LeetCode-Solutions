class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        lst = []
        for i in range(len(nums)):
            lst = list(map(int, str(nums[i])))
            if sum(lst) == i:
                return i
        return -1