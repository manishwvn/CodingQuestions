class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [[nums[0]]]
        
        result = []
        
        def helper(nums, perm):
            if len(perm) == length:
                result.append(perm.copy())
            
            for i in range(len(nums)):
                perm.append(nums[i])
                helper(nums[:i] + nums[i+1:], perm)
                perm.pop()
        
        length = len(nums)
        helper(nums, [])
        return result
        
        