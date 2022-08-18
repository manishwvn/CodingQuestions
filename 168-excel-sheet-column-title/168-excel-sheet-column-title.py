class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        col_title = ""
        n = columnNumber
        
        while n:
            n -= 1
            strn = chr(n % 26 + 65)
            col_title += strn
            n //= 26
            
        return col_title[::-1]
        
        
        