class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        maxm = inc = dec = 1

        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                inc += 1
                dec = 1

            elif nums[i+1] < nums[i]:
                inc = 1
                dec += 1

            else:
                inc = dec = 1

            maxm = max(maxm, inc, dec)
        return maxm
        