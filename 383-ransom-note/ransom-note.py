from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = Counter(magazine)
        for char in ransomNote:
            if char in hm and hm[char] != 0:
                hm[char] -=1
            else:
                return False
        return True
        