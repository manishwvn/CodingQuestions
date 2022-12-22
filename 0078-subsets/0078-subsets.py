class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def backtrack(pos, path):
            result.append(path.copy())
            
            for i in range(pos, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        
        pos, path = 0, []
        
        backtrack(pos, path)
        return result
        