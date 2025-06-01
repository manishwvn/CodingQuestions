class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return (i + 1, j)

        start, end = 0, 0

        for i in range(len(s)):
            l1, r1 = expand(i, i)       
            l2, r2 = expand(i, i + 1)   

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end]