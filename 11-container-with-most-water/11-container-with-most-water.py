class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        m_a = min(height[left], height[right]) * abs(right - left)
        c_a = 0
        while left <= right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
            c_a = min(height[left], height[right]) * abs(right - left)
            m_a = max(c_a, m_a)
    
        return m_a
        
        