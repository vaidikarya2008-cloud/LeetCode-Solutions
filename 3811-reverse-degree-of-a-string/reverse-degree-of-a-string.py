class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        x=0
        for i in range(len(s)):
            x = 26 - (ord(s[i]) - ord('a'))
            x=x*(i+1)
            ans+=x
        return ans
        