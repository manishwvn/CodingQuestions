class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0: return 0

        # dp array O(n) space
        result = 0
        left_walls, right_walls = [0] * len(height), [0] * len(height)
        left_walls[0] = height[0]
        right_walls[-1] = height[-1]

        for i in range(1, len(height)):
            left_walls[i] = max(height[i], left_walls[i-1])
        
        for i in range(len(height)-2, -1, -1):
            right_walls[i] = max(height[i], right_walls[i+1])

        for i in range(1, len(height) - 1):
            result += min(left_walls[i], right_walls[i]) - height[i]
            
        return result