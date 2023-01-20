class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        res = diff = 0
        dp = {0: -1}
        
        for i, num in enumerate(nums):
            diff += (1 if num == 0 else -1)
            if diff in dp:
                res = max(res, i-dp[diff])
            else:
                dp[diff] = i
            
        return res