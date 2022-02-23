class MaxStack:

    def __init__(self):
        self.stack =[]
        self.max_stack = []

    def push(self, x: int) -> None:
        
        if len(self.max_stack) == 0 or x >= self.max_stack[-1]:
            self.max_stack.append(x)
            
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.max_stack:
            if self.stack[-1] == self.max_stack[-1]:
                self.max_stack.pop()
            
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]
        

    def popMax(self) -> int:
        curr_max = self.peekMax()
        temp = []
        
        while(self.stack[-1] != curr_max):
            val = self.stack.pop()
            temp.append(val)
            
        self.pop()
        
        while(temp):
            val = temp.pop()
            self.push(val)
            
        return curr_max
            
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()