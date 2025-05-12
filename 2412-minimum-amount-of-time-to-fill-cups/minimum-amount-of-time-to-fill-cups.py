class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = sum(amount)
        max_val = max(amount)
        return max(max_val, (total + 1) // 2)