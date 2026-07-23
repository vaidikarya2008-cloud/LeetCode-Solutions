class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        final = []

        for i in range(len(nums)):
            if nums[i] != val:
                final.append(nums[i])

        for i in range(len(final)):
            nums[i] = final[i]

        return len(final)