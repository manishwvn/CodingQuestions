class StockPrice:

    def __init__(self):
        self.latest_time = 0
        self.time_to_price = {}
        
        self.min_heap = []
        self.max_heap = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.time_to_price[timestamp] = price
        self.latest_time = max(timestamp, self.latest_time)
        
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.time_to_price[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]
        
        while -price != self.time_to_price[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
            
        return -price
        

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]
        
        while price != self.time_to_price[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
            
        return price
        
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()