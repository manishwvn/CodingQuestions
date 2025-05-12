class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq = Counter(nums)
        unique = list(freq.items())  # (val, count)
        
        total = 0
        left = 0
        n = len(nums)

        for _, count_mid in unique:
            right = n - left - count_mid
            total += left * count_mid * right
            left += count_mid

        return total