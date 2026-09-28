class Solution:
    def maxDepth(self, s: str) -> int:
        lst=[]
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            elif s[i]==')':
                count-=1
            lst.append(count)
        return max(lst)