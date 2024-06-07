class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        curr, maxm = 0, 0
        for account in accounts:
            curr = sum(account)
            maxm = max(curr, maxm)

        return maxm
        