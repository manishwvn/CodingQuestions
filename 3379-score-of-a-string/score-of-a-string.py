class Solution:
    def scoreOfString(self, s: str) -> int:

        ascii = []
        for char in s:
            ascii.append(ord(char))
        
        res = 0
        for i in range(1,len(ascii)):
            res += abs(ascii[i]- ascii[i-1])
        return res
        