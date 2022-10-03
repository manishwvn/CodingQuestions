class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = len(s)-1
        count = 0
        while start>=0 and s[start] == " ":
            start-=1
    
        while start>=0:
            if s[start] == " ":
                return count
            else: count+=1
            start-=1
        return count
        