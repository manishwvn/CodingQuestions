class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = [0] * 26

        # Count frequencies
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Try removing one occurrence of each character
        for i in range(26):
            if freq[i] == 0:
                continue

            freq[i] -= 1

            # Collect non-zero frequencies into a set
            freq_set = set(f for f in freq if f > 0)

            if len(freq_set) == 1:
                return True

            freq[i] += 1  # Restore

        return False