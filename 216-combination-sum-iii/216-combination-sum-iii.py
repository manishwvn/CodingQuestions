class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        if n < k:
            return []
        
        nums = [i for i in range(1, 10)]
        result = []
        
        def helper(path, n, pos):
            #base
            if n == 0 and len(path) == k:
                result.append(path.copy())
                return 
            
            if n < 0:
                return
            
            
            #logic
            prev = -1
            for i in range(pos, len(nums)):
                if nums[i] != prev:
                    path.append(nums[i])
                    helper(path, n - nums[i], i+1)
                    path.pop()
                    prev = nums[i]
                
        
        helper([], n, 0)
        return result
        
        