class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = j = 0
        m, n = len(word1), len(word2)

        while i < m or j < n:
            if i < m:
                result = result + word1[i]
                i += 1
            if j < n:
                result = result + word2[j]
                j += 1

        return result