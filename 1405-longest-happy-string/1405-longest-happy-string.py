from heapq import *
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        result, heap = "", []
        
        for count, char in ((-a, "a"), (-b, 'b'), (-c, 'c')):
            if count:
                heappush(heap, (count, char))
                
        while heap:
            count, char = heappop(heap)
            
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not heap:
                    break
            
                count2, char2 = heappop(heap)
                result += char2
                count2 += 1

                if count2:
                    heappush(heap, (count2, char2))
                
            else:
                result += char
                count += 1
                
            if count:
                heappush(heap, (count, char))
        
        return result
            
            
        