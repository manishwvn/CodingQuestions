class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        n = len(pref)
        count = 0

        for word in words:
            if pref == word[:n]:
                count += 1
        
        return count
        