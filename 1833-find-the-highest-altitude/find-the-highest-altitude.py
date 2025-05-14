class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        alts = [0] * (len(gain) + 1)

        for i in range(len(gain)):
            alts[i+1] = alts[i] + gain[i]

        return max(alts)

        