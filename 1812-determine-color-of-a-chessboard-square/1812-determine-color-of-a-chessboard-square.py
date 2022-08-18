class Solution:
    def squareIsWhite(self, c: str) -> bool:
        
        if c[0] in "aceg":
            return int(c[1]) % 2 == 0
        if c[0] in "bdfh":
            return int(c[1]) % 2 == 1
        