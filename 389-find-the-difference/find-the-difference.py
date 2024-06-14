from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = Counter(s)
        for ch in t:
            if ch not in counts or counts[ch] == 0:
                return ch
            else:
                counts[ch] -= 1