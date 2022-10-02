from heapq import *
class Solution:
    def frequencySort(self, s: str) -> str:
        
        counts = Counter(s)
        heap = []
        
        for key, val in counts.items():
            heappush(heap, [-val, key])
            
        result = ""
        while heap:
            val, key = heappop(heap)
            val = -val
            result += key * val
            
        return result
            
        