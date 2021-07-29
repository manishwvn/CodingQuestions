class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHorizontalDifference = max(horizontalCuts[0], h - horizontalCuts[-1])
        maxVerticalDifference = max(verticalCuts[0], w - verticalCuts[-1])
        
    
        
        for i in range(1, len(horizontalCuts)):
            currentDiff = horizontalCuts[i] - horizontalCuts[i-1]
            if currentDiff > maxHorizontalDifference:
                maxHorizontalDifference = currentDiff
                
        for i in range(1, len(verticalCuts)):
            currentDiff = verticalCuts[i] - verticalCuts[i-1]
            if currentDiff > maxVerticalDifference:
                maxVerticalDifference = currentDiff
                
        return (maxHorizontalDifference * maxVerticalDifference) % (10**9 + 7)
                
        
            
            
        
        
        