class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        result = 0
        n = len(height)
        
        dp_left, dp_right = [0] * n, [0] * n
        
        dp_left[0], dp_right[n - 1] = height[0], height[n-1]
        
        for i in range(1, n):
            dp_left[i] = max(height[i], dp_left[i - 1])
            
        print(dp_left)
        
        
        for i in range(n-2, -1, -1):
            dp_right[i] = max(height[i], dp_right[i+1])
            
        print(dp_right)
        
        
        for i in range(n):
            result += (min(dp_left[i], dp_right[i]) - height[i])
            
        return result
        
        
        
            
        
        
        
        