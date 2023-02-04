class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):    
        self.cap = capacity
        self.cache = {}
        self.lru = Node(-1,-1)
        self.mru = Node(-1, -1)
        
        self.lru.next = self.mru
        self.mru.prev = self.lru
        
    def insert(self, node):
        prevNode, nextNode = self.mru.prev, self.mru
        prevNode.next = node
        nextNode.prev = node
        
        node.prev = prevNode
        node.next = nextNode
        
        
    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
    
    
    
    def get(self, key: int) -> int:
        
        #check if key in cache
        if key in self.cache:
            
            #update the most recent
            
            #1. remove the node
            self.remove(self.cache[key])
            
            #2. insert the node back
            self.insert(self.cache[key])
            
            #return the node
            return self.cache[key].val
            
        #else
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        #check if key in cache then update the value
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        
        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)