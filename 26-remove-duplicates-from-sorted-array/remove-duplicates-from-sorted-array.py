class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst=[]
        for i in range(len(nums)):
            if nums[i]  not in lst:
                lst.append(nums[i])
            else:
                continue
        for i in range(len(lst)):
            nums[i] = lst[i]

        return len(lst)
    