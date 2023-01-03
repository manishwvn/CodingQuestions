class MedianFinder:

    def __init__(self):
        
        self.minHeap,self.maxHeap = [], []
        heapify(self.minHeap)
        heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        
        n = -heappop(self.maxHeap)
        heappush(self.minHeap, n)
        
        if len(self.minHeap) > len(self.maxHeap):
            n = heappop(self.minHeap)
            heappush(self.maxHeap, -n)

    def findMedian(self) -> float:
        
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()