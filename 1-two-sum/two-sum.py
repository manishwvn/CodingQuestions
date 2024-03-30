class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2: return [0, 1]

        diffs = {}
        for i in range(0, len(nums)):
            if target - nums[i] in diffs:
                return [i, diffs[target - nums[i]]]
            else:
                diffs[nums[i]] = i



        