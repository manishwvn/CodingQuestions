class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        if len(s) == 1: return True

        counts = Counter(s)

        base = counts[s[0]]

        for v in counts.values():
            if v != base:
                return False

        return True
        