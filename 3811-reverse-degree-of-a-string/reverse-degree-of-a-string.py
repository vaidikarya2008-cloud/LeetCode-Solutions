class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            ordinate=ord(s[i])-ord("a")
            ans+=(26-ordinate)*(i+1)
        return ans