class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        m, n = len(accounts), len(accounts[0])
        wealths = [-1] * m

        for i in range(m):
            wealths[i] = sum(accounts[i])

        return max(wealths)
            

        