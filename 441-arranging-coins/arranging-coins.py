class Solution:
    def arrangeCoins(self, n: int) -> int:

        i = 1
        count = 0
        while n > 0:
            if n - i < 0:
                return count
            n -= i 
            i += 1
            count += 1

        return count


        