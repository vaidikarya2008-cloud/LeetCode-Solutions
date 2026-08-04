class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxi=max(nums)
        mini=min(nums)
        lst=[]
        for i in range(mini,maxi,1):
            if i not in nums:
                lst.append(i)        
        return lst