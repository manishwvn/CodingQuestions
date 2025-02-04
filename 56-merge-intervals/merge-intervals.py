class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        if len(intervals) == 1:
            return intervals
        
        
        intervals.sort()
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            
            last = result[-1][1]
            
            if intervals[i][0] <= last:
                result[-1][1] = max(last, intervals[i][1]) 
                
            else:
                result.append(intervals[i])
                
        return result
        
        