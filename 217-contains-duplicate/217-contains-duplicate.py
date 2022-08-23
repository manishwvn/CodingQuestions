class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = collections.Counter(nums)
        for num in nums:
            if hm[num] >= 2:
                return True
            
        return False
        