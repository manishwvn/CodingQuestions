class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        is_negative = num < 0
        num = abs(num)
        result = ""
        
        while num > 0:
            digit = num % 7
            result = str(digit) + result
            num //= 7
        
        if is_negative:
            result = "-" + result
        
        return result