class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        if n == k == 1:
            return [[1]]
        
        result = []
        
        def helper(pivot, comb):
            #base
            if len(comb) == k:
                result.append(comb.copy())
                return 
            
            #logic
            for i in range(pivot, n+1):
                comb.append(i)
                helper(i+1, comb)
                comb.pop()
        
        helper(1, [])
        return result
        