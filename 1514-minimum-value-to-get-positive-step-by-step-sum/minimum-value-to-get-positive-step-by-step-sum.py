class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        prefix_sum = [None] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        min_val = min(prefix_sum)

        if min_val < 1:
            return 1 - min_val
        else:
            return 1
        