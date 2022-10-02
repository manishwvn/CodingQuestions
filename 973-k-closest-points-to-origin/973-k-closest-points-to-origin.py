from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        origin = [0, 0]
        heap = []
        
        for point in points:
            euc_dist = math.dist(point, origin)
            heappush(heap, (euc_dist, point))
            
        closest = nsmallest(k, heap)
        result = []
        for point in closest:
            result.append(point[1])
            
        return result
        
        
        
        