class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ch = 0
        for char in s:
            ch ^= ord(char)

        for char in t:
            ch ^= ord(char)

        return chr(ch)