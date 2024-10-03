class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False
        
        numset = set()
        
        for num in nums:
            if num in numset: 
                return True
            else:
                numset.add(num)

        return False
