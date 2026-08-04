class Solution:
    def minElement(self, nums: List[int]) -> int:
        lst = []

        for i in range(len(nums)):
            total = 0
            for dig in str(nums[i]):
                total += int(dig)
            lst.append(total)

        return min(lst)