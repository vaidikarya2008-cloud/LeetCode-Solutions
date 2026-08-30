class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        ans=[]
        mini = min(nums)
        maxi = max(nums)
        mini_index = nums.index(mini)
        maxi_index = nums.index(maxi)
        ans.append(max(mini_index, maxi_index) + 1)
        ans.append(len(nums) - min(mini_index, maxi_index))
        ans.append(min(mini_index, maxi_index) + 1 +
                len(nums) - max(mini_index, maxi_index))

        return min(ans)