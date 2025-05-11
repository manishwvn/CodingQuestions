class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left, right = 0, int(sqrt(c))

        while left <= right:

            total = left * left + right * right

            if total == c:
                return True

            elif total > c:
                right -= 1
            else:
                left += 1

        return False
