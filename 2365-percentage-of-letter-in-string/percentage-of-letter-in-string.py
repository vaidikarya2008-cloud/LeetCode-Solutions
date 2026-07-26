class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        lenth=len(s)
        count=0
        lst=list(s)
        for i in range(len(lst)):
            if lst[i]==letter:
                count+=1
            else:
                count+=0
        return round((count*100)//lenth)
        