class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        counts = Counter(s)

        count = 0
        for key, value in counts.items():
            count += value % 2
        
        return count <= 1
        