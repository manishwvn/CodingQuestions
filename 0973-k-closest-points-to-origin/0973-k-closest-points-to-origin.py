class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        heap = []
        
        for i in range(len(points)):
            
            dist = math.sqrt((points[i][0])**2 + (points[i][1])** 2)
            
            heappush(heap, (dist, points[i]))
            
        result = []
        
        while k:
            dist, point = heappop(heap)
            result.append(point)
            k -= 1
            
        return result