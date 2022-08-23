class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}
        
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec in hm:
                return [i, hm[sec]]
            else:
                hm[nums[i]] = i