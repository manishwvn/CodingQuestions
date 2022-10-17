class Node:
    
    def __init__(self, url):
        self.val = url
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.start = Node(homepage)
        

    def visit(self, url: str) -> None:
        node = Node(url)
        self.start.next = node
        node.prev = self.start
        self.start = self.start.next
        

    def back(self, steps: int) -> str:
        while steps and self.start.prev:
            self.start = self.start.prev
            steps -= 1
            
        return self.start.val
        

    def forward(self, steps: int) -> str:
        while steps and self.start.next:
            self.start = self.start.next
            steps -=1
            
        return self.start.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)