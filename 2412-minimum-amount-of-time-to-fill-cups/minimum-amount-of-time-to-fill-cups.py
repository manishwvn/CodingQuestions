import heapq
from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Convert to max heap by pushing negative values
        max_heap = [-a for a in amount if a > 0]
        heapq.heapify(max_heap)
        
        seconds = 0

        while max_heap:
            first = -heapq.heappop(max_heap)

            if max_heap:
                second = -heapq.heappop(max_heap)
                first -= 1
                second -= 1
                seconds += 1
                if first > 0:
                    heapq.heappush(max_heap, -first)
                if second > 0:
                    heapq.heappush(max_heap, -second)
            else:
                # Only one type left
                seconds += first
                break

        return seconds