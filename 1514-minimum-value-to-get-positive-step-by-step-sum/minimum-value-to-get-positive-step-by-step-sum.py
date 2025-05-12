class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return abs(nums[0]) + 1 if nums[0] < 1 else 1

        prefix_sum = 0
        min_val = float("inf")
        for num in nums:
            prefix_sum += num
            min_val = min(min_val, prefix_sum)

        return abs(min_val) + 1 if min_val < 0 else 1
        