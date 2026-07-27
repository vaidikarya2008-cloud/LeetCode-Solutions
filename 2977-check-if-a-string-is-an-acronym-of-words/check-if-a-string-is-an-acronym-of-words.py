class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        lst=list(s)
        count=0
        if len(s)==len(words):
            for i in range(len(words)):
                if words[i].startswith(lst[i]):
                    count+=1
                else:
                    continue
            if count == len(lst):
                return True
            else:
                return False
        else:
            return False
            