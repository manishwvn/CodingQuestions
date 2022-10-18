class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        result = 0
        l, r = 0, len(height) - 1
        lw, rw = 0, 0 
        
        while l <= r:
            
            if lw <= rw:
                #explore on left side
                if height[l] < lw:
                    #trap the water
                    result += (lw - height[l])
                    
                else:
                    lw = height[l]
                    
                l += 1
                
            else:
                #explore on right side
                if height[r] < rw:
                    result += rw - height[r]
                    
                else:
                    rw = height[r]
                    
                r -= 1
                
        return result
                    
            
                    
                