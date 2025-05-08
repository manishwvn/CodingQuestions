class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        res = [None] * len(nums)

        for i in range(len(res)):
            res[i] = nums[nums[i]]

        return res
        