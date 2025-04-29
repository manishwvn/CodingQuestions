class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        res = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):

                    if i < j < k:
                        curr = max((nums[i] - nums[j]) * nums[k], 0)
                        res = max(curr, res)

        return res
        