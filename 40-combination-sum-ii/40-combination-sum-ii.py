class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []
        
        candidates.sort()
        result = []
        
        def helper(candidates, pivot, amount, path):
            #base
            if amount == 0:
                result.append(path.copy())
                return
            
            if amount < 0:
                return 
            
            #logic
            prev = -1
            for i in range(pivot, len(candidates)):
                if candidates[i] != prev:
                    path.append(candidates[i])
                    helper(candidates, i + 1, amount - candidates[i], path)
                    path.pop()
                    prev = candidates[i]
        
        helper(candidates, 0, target, [])
        return result
        
        