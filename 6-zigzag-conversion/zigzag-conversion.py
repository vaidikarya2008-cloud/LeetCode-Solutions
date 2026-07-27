class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        start = 0
        direction = 1
        lst = []

        for i in range(numRows):
            lst.append("")

        for i in range(len(s)):
            lst[start] += s[i]

            if start == numRows - 1:
                direction = -1
            elif start == 0:
                direction = 1
            
            start += direction

        return "".join(lst)