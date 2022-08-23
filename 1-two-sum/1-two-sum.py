class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}
        
        for i in range(len(nums)):
            j = target - nums[i]
            if j in hm:
                return [i, nums.index(j)]
            else:
                hm[nums[i]] = True