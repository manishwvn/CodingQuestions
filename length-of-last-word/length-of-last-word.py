class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        ls = s.split()
        if len(ls) == 0:
            return 0
        return len(ls[-1])
        