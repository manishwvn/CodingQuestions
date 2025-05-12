class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        freq = [0] * 1001  # Since nums[i] in 1 to 1000

        for num in nums:
            freq[num] += 1

        total = 0
        left = 0
        n = len(nums)

        for count_mid in freq:
            if count_mid == 0:
                continue
            right = n - left - count_mid
            total += left * count_mid * right
            left += count_mid

        return total