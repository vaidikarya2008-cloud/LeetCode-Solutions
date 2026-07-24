class Solution:
    def maxProduct(self, n: int) -> int:
        lst = list(map(int, str(n)))
        lst1=lst.sort()
        for i in range(len(lst)):
            return(lst[-1]*lst[-2])

        