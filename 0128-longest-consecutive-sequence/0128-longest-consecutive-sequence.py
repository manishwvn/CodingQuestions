class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_streak = 0
        
        for n in nums:
            if n - 1 not in num_set:
                length = 0
                while n+length in num_set:
                    length +=1
                    
                max_streak = max(max_streak, length)
        
        return max_streak
                