class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []

        for i in range(1, n + 1):
            if i in target:
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")

            if i == target[-1]:
                break

        return ans