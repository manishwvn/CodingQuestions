from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #for loop based recursion with backtracking
        
        """
        n = number of elems
        m = target
        Time Complexity: O(2 ^ (m*n)) 
        Space Complexity: O(2 ^ (m*n))
        """
        
        if not candidates:
            return result
        
        result = []
        def helper(candidates, amount, path, pivot):
            #base
            if amount == 0:
                result.append(path.copy())
                return
            
            if amount < 0:
                return 
            
            #logic
            for i in range(pivot, len(candidates)):
                path.append(candidates[i])
                helper(candidates, amount - candidates[i], path, i)
                path.pop()
                
        
        helper(candidates, target, [], 0)
        return result
        
        