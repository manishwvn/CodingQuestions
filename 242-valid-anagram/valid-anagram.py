class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are equal
        if len(s) != len(t):
            return False
        
        # Create a fixed-size array to store character counts
        char_counts = [0] * 26
        
        # Increment counts for characters in s
        for char in s:
            char_counts[ord(char) - ord('a')] += 1
        print(char_counts)
        
        # Decrement counts for characters in t
        for char in t:
            char_counts[ord(char) - ord('a')] -= 1
        print(char_counts)
        
        # If all counts are zero, strings are anagrams
        return all(count == 0 for count in char_counts)