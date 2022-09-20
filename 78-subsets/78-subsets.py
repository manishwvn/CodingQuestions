class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def helper(pos, subset):
            if len(subset) == len(nums):
                result.append(subset.copy())
                return
            else:
                result.append(subset.copy())
                for i in range(pos, len(nums)):
                    subset.append(nums[i])
                    helper(i+1, subset)
                    subset.pop()
        
        # for i in range(len(nums)+1):
        helper(0, [])
        return result