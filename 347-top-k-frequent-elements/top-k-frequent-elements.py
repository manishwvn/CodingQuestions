class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #2nd approach: using minheap TC = O(nlogk) SC = O(n + k)
        #1. find counts
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        #2. create heap and append k counts
        heap = []
        for key, val in counts.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)

        #3.create res and append values of heap
        res = []
        while heap:
            res.append(heappop(heap)[1])

        return res
        