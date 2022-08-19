def bs(nums, target, bias):
    l, r, i = 0, len(nums) - 1, -1
    
    while l <= r:
        
        m = (l + r) // 2
        
        if target > nums[m]:
            l = m + 1
            
        elif target < nums[m]:
            r = m - 1
            
        else:
            i = m
            if bias:
                r = m - 1
            else:
                l = m + 1
    return i

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = bs(nums, target, True)
        r = bs(nums, target, False)
        return [l, r]
        