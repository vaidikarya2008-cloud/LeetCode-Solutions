class Solution:
    def checkDivisibility(self, n: int) -> bool:
        lst = list(map(int, str(n)))
        sum=0
        multi=1
        for i in range(len(lst)):
            multi*=lst[i]
            sum+=lst[i]
        if n % (sum + multi) == 0:
            return True
        else:
            return False