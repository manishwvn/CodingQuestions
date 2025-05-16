class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        #get total counts of a, b, c:
        total = [0, 0, 0]

        for char in s:
            total[ord(char) - ord('a')] += 1

        #check if s is valid
        if min(total) < k: return -1
        
        #sliding window

        res = len(s)
        l = 0 
        for r in range(len(s)):
            total[ord(s[r]) - ord('a')] -= 1

            while min(total) < k:
                total[ord(s[l]) - ord('a')] += 1
                l += 1

            res = min(res, len(s) - (r - l + 1))

        return res