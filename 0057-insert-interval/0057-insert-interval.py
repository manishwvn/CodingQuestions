class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        
        result = [intervals[0]]
        
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            
            last_end = result[-1][1]
            
            if start <= last_end:
                result[-1][1] = max(end, last_end)
                
            else:
                result.append([start, end])
                
        return result
                
        