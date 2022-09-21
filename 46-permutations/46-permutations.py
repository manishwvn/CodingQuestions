class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        hm = Counter(nums)
        
        def helper(perm, hm):
            if len(perm) == len(nums):
                result.append(perm.copy())
                return 
            
            #action
            for num in hm:
                if hm[num] == 0:
                    continue
                
                perm.append(num)
                hm[num] -= 1
            #recursion
                helper(perm, hm)
                
            #backtrack
                hm[num] += 1
                perm.pop()
                
        helper([], hm)
        return result
        