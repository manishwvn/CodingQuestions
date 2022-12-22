class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        heap = []
        result = []
        
        for num, count in counts.items():
            heappush(heap, (-count, num))
            
        while heap and k > 0:
            count, num = heappop(heap)
            result.append(num)
            k -= 1
                
        return result
            