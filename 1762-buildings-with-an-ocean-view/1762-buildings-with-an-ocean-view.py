class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        result = []
        maxm = -float("inf")
        
        for i in range(len(heights) - 1, -1, -1):
            curr = heights[i]
            if curr > maxm:
                result.append(i)
                maxm = curr
                
        return result[::-1]
            
        
        
        