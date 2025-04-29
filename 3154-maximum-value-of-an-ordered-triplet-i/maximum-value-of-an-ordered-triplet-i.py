class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        res = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    curr = max((nums[i] - nums[j]) * nums[k], 0)
                    res = max(curr, res)

        return res
        