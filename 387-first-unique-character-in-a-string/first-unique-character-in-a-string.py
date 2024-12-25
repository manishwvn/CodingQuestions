class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}

        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = [i]
            else:
                hm[s[i]].append(i)

        for char in s:
            if len(hm[char]) == 1:
                return hm[char][0]
        
        return -1