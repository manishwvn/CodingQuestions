class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getNextNum(n):
            digitSum = 0
            
            while n > 0:
                d = n % 10
                n = n // 10
                digitSum += d ** 2
                
            return digitSum
        
        seenNums = set()
        while n != 1 and n not in seenNums:
            seenNums.add(n)
            n = getNextNum(n)
            
        return n == 1
        