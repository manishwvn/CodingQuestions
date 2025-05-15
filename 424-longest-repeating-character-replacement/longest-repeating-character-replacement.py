class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #inefficient sliding window
        max_len = 0
        l = 0
        counts = [0] * 26
        for r in range(len(s)):
            counts[ord(s[r]) - ord('A')] += 1
            # freq = Counter(substr)
            max_freq = max(counts)

            # change = len(substr) - max_freq
            change = r - l + 1 - max_freq

            if change > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                max_len = max(max_len, r - l + 1)
        return max_len