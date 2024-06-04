class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s: return True
        if not t: return False
        if len(s) > len(t): return False

        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return True if i == len(s) else False

        