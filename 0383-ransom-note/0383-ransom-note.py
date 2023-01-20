class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        counts = Counter(magazine)
        
        for char in ransomNote:
            if char not in counts or counts[char] == 0:
                return False
            
            counts[char] -= 1
            
        return True
            
                
        