class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def helper(i, path, target):
            # base case
            if target == 0:
                result.append(path.copy())
                return

            if target < 0 or i == len(nums):
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                helper(j, path, target - nums[j])
                path.pop()            

        helper(0, [], target)
        return result
        