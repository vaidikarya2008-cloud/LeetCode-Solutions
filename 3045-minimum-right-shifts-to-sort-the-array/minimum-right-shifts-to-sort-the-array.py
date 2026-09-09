class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:

        count = 0

        while count < len(nums):

            if nums == sorted(nums):
                return count

            last = nums[-1]

            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = last

            count += 1

        return -1