class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        curr = 0
        high = 0

        for g in gain:
            curr += g
            high = max(curr, high)
        return high