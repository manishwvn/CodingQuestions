class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #binary search approach
        #[0, 1, 3]
        #nums[m] = t
        
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= m:
                l = m + 1
            else:
                ans = m
                r = m - 1
    
        return l if ans == -1 else ans
                
            