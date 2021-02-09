class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        sumn = (n * (n+1)) / 2
        sumarr = sum(nums)
        
        return int(sumn - sumarr)
        