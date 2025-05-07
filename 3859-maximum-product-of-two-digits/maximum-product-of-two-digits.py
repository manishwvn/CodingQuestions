class Solution:
    def maxProduct(self, n: int) -> int:

        digits = []
        while n:
            rem = n % 10
            digits.append(rem)
            n //= 10

        digits.sort(reverse=True)
        return digits[0] * digits[1]

        