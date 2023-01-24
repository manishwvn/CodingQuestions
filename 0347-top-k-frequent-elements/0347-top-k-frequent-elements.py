class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        nums = Counter(nums)
        heap = []
        res = []
        
        for num, count in nums.items():
            heappush(heap, (-count, num))
            
        while k:
            count, num = heappop(heap)
            res.append(num)
            k -= 1
                
        return res
            
            
            
        