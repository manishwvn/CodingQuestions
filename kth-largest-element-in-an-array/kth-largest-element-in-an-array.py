from heapq import heappush, heappop, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        heapify(nums)
        count = 0
        
        while nums:
            if count == n - k:
                return heappop(nums)
            else:
                heappop(nums)
                count += 1
        
        