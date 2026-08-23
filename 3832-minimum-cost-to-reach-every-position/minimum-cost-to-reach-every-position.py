class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minimum = cost[0]
        ans = []

        for i in range(len(cost)):
            if cost[i] < minimum:
                minimum = cost[i]

            ans.append(minimum)

        return ans