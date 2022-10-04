class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        
        #if values of small heap > values of large heap
        if (self.small and self.large) and (-self.small[0] > self.large[0]):
            value = -heappop(self.small)
            heappush(self.large, value)
            
        #if lengths are uneven:
        if len(self.small) > len(self.large) + 1:
            value = -heappop(self.small)
            heappush(self.large, value)
            
        if len(self.large) > len(self.small) + 1:
            value = heappop(self.large)
            heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0] + self.large[0]) / 2
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()