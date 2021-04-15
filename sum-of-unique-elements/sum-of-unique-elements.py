class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        hm = {}
        for num in nums:
            hm[num] = nums.count(num)
            
        result = 0
        for key, value in hm.items():
            if value == 1:
                result += key
                
        return result