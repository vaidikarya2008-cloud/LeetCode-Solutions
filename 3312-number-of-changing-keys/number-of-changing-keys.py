class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        for i in range(len(s)-1):
            if s[i+1]==s[i].lower() or s[i+1]==s[i].upper():
                count+=0
            else:
                count+=1
        return count
