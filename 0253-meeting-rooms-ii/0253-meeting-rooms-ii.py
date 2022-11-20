class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        
        result, count = 0, 0
        s, e = 0, 0
        
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
                
            else:
                e += 1
                count -= 1
                
            result = max(result, count)
            
        return result
        
        