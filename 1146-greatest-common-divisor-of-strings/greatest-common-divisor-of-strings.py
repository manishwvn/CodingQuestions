class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        
        if str1 + str2 != str2 + str1:
            return ""
        
        l = gcd(len(str1), len(str2))
        return str1[:l]
        