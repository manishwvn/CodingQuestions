class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        k = 1
        while n >= k:
            n -= k
            k += 1
            count += 1
        return count


        