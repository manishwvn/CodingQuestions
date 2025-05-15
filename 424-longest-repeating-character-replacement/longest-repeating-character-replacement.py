from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #generalized
        counts = defaultdict(int)
        max_len = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])

            # window_size - max_freq = number of changes needed
            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len