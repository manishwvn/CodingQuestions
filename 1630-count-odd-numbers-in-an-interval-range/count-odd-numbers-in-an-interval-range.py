class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = (high - low) // 2

        if low % 2 != 0 or high % 2 != 0:
            odd += 1

        return odd
        