from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #unoptimized
        if not candidates:
            return result
        
        result = []
        def helper(candidates, amount, path, i):
            #base
            if amount == 0:
                result.append(path)
                return
            
            if amount < 0 or i == len(candidates):
                return 
            
            #logic
            #not choose
            helper(candidates, amount, deepcopy(path), i + 1)
            
            #choose
            path.append(candidates[i])
            helper(candidates, amount - candidates[i], deepcopy(path), i)
        
        helper(candidates, target, [], 0)
        return result
        
        