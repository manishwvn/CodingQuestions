class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        heap = []
        
        for i in range(len(points)):
            
            dist = math.sqrt((points[i][0])**2 + (points[i][1])** 2)
            
            heappush(heap, (-dist, points[i]))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [ele[1] for ele in heap]