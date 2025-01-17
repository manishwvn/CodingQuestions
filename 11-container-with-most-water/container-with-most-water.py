class Solution:
    def maxArea(self, height: List[int]) -> int:

        start, end = 0, len(height) - 1

        max_area = 0

        while start < end:
            curr_area = min(height[start], height[end]) * (end - start)
            max_area = max(curr_area, max_area)

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
            
        return max_area


        