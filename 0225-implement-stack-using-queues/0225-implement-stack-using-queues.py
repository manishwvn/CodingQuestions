class MyStack:

    def __init__(self):
        self.stack_queue = deque()
        

    def push(self, x: int) -> None:
        prev_size = len(self.stack_queue)
        
        self.stack_queue.append(x)
        while prev_size > 0:
            popped = self.stack_queue.popleft()
            self.stack_queue.append(popped)
            prev_size -= 1
 
    def pop(self) -> int:
        return self.stack_queue.popleft()
        

    def top(self) -> int:
        return self.stack_queue[0]

    def empty(self) -> bool:
        return False if self.stack_queue else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()