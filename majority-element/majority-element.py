class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
                
                
        n = len(nums)
        n = n // 2
        
        for val in hm:
            if hm[val] > n:
                return val