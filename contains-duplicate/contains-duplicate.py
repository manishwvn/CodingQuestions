class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
                
        for num in hm:
            if hm[num] >= 2:
                return True
            
            
        return False
        