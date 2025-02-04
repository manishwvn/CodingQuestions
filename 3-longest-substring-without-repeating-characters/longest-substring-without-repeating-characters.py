class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Stores last seen index of each character
        i = 0  # Left pointer
        length = 0  # Max length

        for j in range(len(s)):
            if s[j] in char_index and char_index[s[j]] >= i:
                i = char_index[s[j]] + 1  # Move `i` past the last occurrence

            char_index[s[j]] = j  # Update last seen index
            length = max(length, j - i + 1)  # Track max substring length

        return length