class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        curr_max, maxm = nums[0], nums[0]
        r = 1

        while r < len(nums):
            if nums[r] > nums[r - 1]:
                curr_max += nums[r]
            else:
                curr_max = nums[r]
            r += 1
            maxm = max(curr_max, maxm)
        return maxm

        