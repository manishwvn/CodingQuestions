class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        lookup = set(chr(i) for i in range(97, 123))
        charSet = set(char for char in sentence)
        
        return charSet == lookup
        