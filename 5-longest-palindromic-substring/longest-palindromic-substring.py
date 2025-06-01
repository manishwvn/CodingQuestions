class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1: return s

        def expand(i, j):
            left, right = i, j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return (left + 1, right)

        max_len = 0
        res = ""

        for i in range(len(s) - 1):
            left, right = expand(i, i)
            
            if right - left > max_len:
                max_len = right - left
                res = s[left:right]

            left, right = expand(i, i + 1)
            if right - left > max_len:
                max_len = right - left
                res = s[left:right]

        return res


        

        
        