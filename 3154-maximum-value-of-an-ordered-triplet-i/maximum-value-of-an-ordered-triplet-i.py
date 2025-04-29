class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        i, res = 0, 0

        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[j] > nums[i]:
                    i = j
                res = max(res, (nums[i] - nums[j]) * nums[k])

        return res
        