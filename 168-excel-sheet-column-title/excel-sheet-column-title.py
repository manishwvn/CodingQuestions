class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        if columnNumber <= 26:
            return chr(ord('A') + columnNumber - 1)

        result = ""

        while columnNumber:
            rem = (columnNumber - 1) % 26
            print(chr(ord('A') + rem))
            result += chr(ord('A') + rem)
            columnNumber  = (columnNumber - 1) // 26

        return result[::-1]


        