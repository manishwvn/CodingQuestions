from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #backtracking
        
        """
        n = number of elems
        m = target
        Time Complexity: O(2 ^ (m*n)) 
        Space Complexity: O(2 ^ (m*n))
        """
        
        if not candidates:
            return result
        
        result = []
        def helper(candidates, amount, path, i):
            #base
            if amount == 0:
                result.append(path.copy())
                return
            
            if amount < 0 or i == len(candidates):
                return 
            
            #logic
            #not choose
            helper(candidates, amount, path, i + 1)
            
            #choose
            
            #action
            path.append(candidates[i])
            
            #recursion
            helper(candidates, amount - candidates[i], path, i)
            
            #backtrack
            path.pop()
        
        helper(candidates, target, [], 0)
        return result
        
        