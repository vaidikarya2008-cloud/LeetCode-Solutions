class Solution:
    def arraySign(self, nums: list[int]) -> int:
        checkminus = 0
        checkzero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                checkzero += 1
            elif nums[i] > 0:
                continue
            else:
                checkminus += 1

        if checkzero > 0:
            return 0
        if checkminus % 2 == 0:
            return 1
        else:
            return -1