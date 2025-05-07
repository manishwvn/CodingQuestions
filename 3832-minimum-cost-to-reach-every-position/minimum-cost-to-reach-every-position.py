class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:

        res = [0] * len(cost)
        res[0] = cost[0]

        for i in range(1, len(cost)):
            res[i] = min(cost[i], res[i-1])

        return res

        