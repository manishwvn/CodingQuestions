class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2: return [0, 1]

        hm = {}
        for i in range(len(nums)):
            if target - nums[i] in hm:
                return [i, hm[target - nums[i]]]
            else:
                hm[nums[i]] = i

        return [-1, -1]
        