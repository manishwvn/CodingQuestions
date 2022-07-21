class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        sum_, prod = 0, 1
        
        while(n):
            digit = n % 10
            sum_ += digit
            prod *= digit
            n //= 10
            
        return prod - sum_
        
        