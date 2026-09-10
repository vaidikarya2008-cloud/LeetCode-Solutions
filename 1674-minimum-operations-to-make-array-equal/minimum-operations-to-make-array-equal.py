class Solution:
    def minOperations(self, n: int) -> int:

        arr = []

        for i in range(1, 2*n, 2):
            arr.append(i)

        middle = arr[len(arr)//2]

        ans = 0

        for i in range(len(arr)):
            ans += abs(middle - arr[i]) // 2

        return ans