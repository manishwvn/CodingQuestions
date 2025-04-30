class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        res = 0

        for num in range(low, high+1):
            if num < 100 and num % 11 == 0:
                res += 1

            if 1000 <= num < 10000:
                left = num // 1000 + num % 1000 // 100
                right = num % 100 // 10 + num % 10
                if left == right:
                    res += 1
        return res
        