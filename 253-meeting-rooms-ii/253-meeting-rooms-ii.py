class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        heap = []
        
        heappush(heap, intervals[0][1])
        count = 1
        
        for i in range(1, len(intervals)):
            
            if heap[0] <= intervals[i][0]:
                heappop(heap)
                count -= 1
                
            heappush(heap, intervals[i][1])
            count += 1
            
        return count
        