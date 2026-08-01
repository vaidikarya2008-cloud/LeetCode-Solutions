class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        lst1=[]
        lst2=[]
        for i in range(len(nums)):
            if nums[i]<10:
                lst1.append(nums[i])
            else:
                lst2.append(nums[i])
        if sum(lst1)>sum(lst2) or sum(lst1)<sum(lst2):
            return True
        else:
            return False
        