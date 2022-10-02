from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        origin = [0, 0]
        heap = []
        
        for point in points:
            euc_dist = math.dist(point, origin)
            heappush(heap, (euc_dist, point))
            
        return [point[1] for point in nsmallest(k, heap)]
        
        
        
        
        