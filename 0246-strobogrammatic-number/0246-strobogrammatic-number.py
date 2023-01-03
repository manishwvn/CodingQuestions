class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
#         def getDigits(n):
#             digits = []
            
#             while n:
#                 rem = n % 10
#                 n //= 10
#                 digits.append(rem)
                
#             return digits
        
        numset = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        l, r = 0, len(num) - 1

        
        while l <= r :
            if num[l] not in numset or num[r] not in numset:
                return False
            
            if numset[num[l]] != num[r]:
                return False
            
            l += 1
            r -= 1
            
        return True
        