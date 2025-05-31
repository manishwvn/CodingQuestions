class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        #using hashmap/counter
        result = []
        counts = Counter(nums)
        
        def helper(perm):
            #base
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            #logic
            for n in counts:
                #action
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1
                    
                    #recursion
                    helper(perm)
                    
                    #backtrack
                    counts[n] += 1
                    perm.pop()
                    
        helper([])
        return result
        