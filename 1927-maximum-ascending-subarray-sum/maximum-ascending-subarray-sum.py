class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        curr_max, maxm = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_max += nums[i]
            else:
                curr_max = nums[i]
            maxm = max(curr_max, maxm)
        return maxm

        