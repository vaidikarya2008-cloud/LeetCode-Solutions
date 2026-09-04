class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans = []

        for i in range(len(nums)):
            maxi = max(nums[:i+1])
            mini = min(nums[i:])

            ans.append(maxi - mini)

        for i in range(len(ans)):
            if ans[i] <= k:
                return i

        return -1