class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        def getDigits(n):
            digits = []
            
            while n:
                rem = n % 10
                n //= 10
                digits.append(rem)
                
            return digits
        
        numset = {0:0, 1:1, 6:9, 8:8, 9:6}
        
        digits = getDigits(int(num))
        
        newnum = 0
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] not in numset:
                return False
            newnum = newnum * 10 + numset[digits[i]]
            
        newnum = str(newnum)
        return newnum[::-1] == num