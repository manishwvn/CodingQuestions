class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        
        
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
                
                
        for num in hm:
            if hm[num] > 1:
                return num
            
            
        
        