class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False
        
        numset = list(set(nums))
        return len(numset) != len(nums)