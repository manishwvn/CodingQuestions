class Solution:
    def countOdds(self, low: int, high: int) -> int:

        range = high - low + 1
        count = range // 2
        if range % 2 and low % 2:
            count += 1
        return count



        