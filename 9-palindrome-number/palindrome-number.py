class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1=list(str(x))
        revlist=[]
        lenth=len(list1)
        for i in range(-1,-lenth-1,-1):
            revlist.append(list1[i])
        if list1==revlist:
            return True
        else:
            return False
        