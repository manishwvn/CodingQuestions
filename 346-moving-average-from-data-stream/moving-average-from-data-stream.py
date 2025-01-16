class MovingAverage:

    def __init__(self, size: int):
        self.nums = deque()
        self.size = size
        self.sum_ = 0
        self.count = 0
        
        
        

    def next(self, val: int) -> float:
        self.nums.append(val)
        self.count += 1
        
        tail = self.nums.popleft() if self.count > self.size else 0
        
        self.sum_ = self.sum_ - tail + val
        
        div = min(self.size, self.count) if self.count else 1
        return self.sum_ / div
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)