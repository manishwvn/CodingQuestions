class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        chars1, chars2 = Counter(word1), Counter(word2)
        
        for i in range(ord("a"), ord("z") + 1):
            freq1, freq2 = chars1[chr(i)], chars2[chr(i)]
            
            if abs(freq1 - freq2) > 3:
                return False
            
            
        return True
        