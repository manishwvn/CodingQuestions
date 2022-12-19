class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        
        for num in nums:
            heappush(heap, -num)
            
        for _ in range(k):
            result = -heapq.heappop(heap)
            
        return result
        