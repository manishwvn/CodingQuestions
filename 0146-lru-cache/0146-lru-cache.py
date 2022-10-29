class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = Node(-1, -1)
        self.mru = Node(-1, -1)
        
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insert(self, node):
        prevNode, nextNode = self.mru.prev, self.mru
        prevNode.next = node
        nextNode.prev = node
        
        node.prev = prevNode
        node.next = nextNode
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            #update to most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        #if node exists, update value
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            #remove from list and delete from cache
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)