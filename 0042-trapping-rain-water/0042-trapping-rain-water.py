class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        result = 0
        
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(height[l], left_max)
                result += left_max - height[l]
                
            else:
                r -= 1
                right_max = max(height[r], right_max)
                result += right_max - height[r]
                
        return result
                
                
        
        