class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j+1]
                count = 0
                check = []

                for k in range(len(subarray)):
                    if subarray[k] in check:
                        continue
                    else:
                        check.append(subarray[k])
                        count += 1

                ans += (count**2)

        return ans