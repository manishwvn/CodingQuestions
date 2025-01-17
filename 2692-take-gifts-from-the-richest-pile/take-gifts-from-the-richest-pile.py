class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        heap = []
        for gift in gifts:
            heap.append(-gift)
        heapify(heap)

        for _ in range(k):
            gift = -heappop(heap)
            heappush(heap, -int(math.sqrt(gift)))
        
        sum_ = 0
        for i in range(len(heap)):
            sum_ += (-heap[i])
        return sum_
        