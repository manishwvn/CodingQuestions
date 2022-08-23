class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = collections.Counter(s)
        for i in range(len(s)):
            if s[i] in hm and hm[s[i]] == 1:
                return i
        return -1
        