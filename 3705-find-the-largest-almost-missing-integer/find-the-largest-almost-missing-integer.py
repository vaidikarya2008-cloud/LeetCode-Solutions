class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        if k == 1:
            ans = -1

            for i in range(len(nums)):
                if nums.count(nums[i]) == 1:
                    ans = max(ans, nums[i])

            return ans

        if k == len(nums):
            return max(nums)

        first = nums[0]
        last = nums[-1]

        count_first = 0
        count_last = 0

        for i in range(len(nums)):
            if nums[i] == first:
                count_first += 1

            if nums[i] == last:
                count_last += 1

        if count_first == 1 and count_last == 1:
            return max(first, last)

        elif count_first == 1:
            return first

        elif count_last == 1:
            return last

        return -1