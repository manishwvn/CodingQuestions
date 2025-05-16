class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr, maxm = 0, 0
        for num in nums:
            if num == 1:
                curr += 1
            maxm = max(curr, maxm)
            if num == 0:
                curr = 0
                
        return maxm
            
        