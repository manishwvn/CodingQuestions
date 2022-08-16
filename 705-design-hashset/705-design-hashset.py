class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [None for _ in range(self.size)]
        
    def hash_value(self, key):
        return key % self.size
    
    def add(self, key: int) -> None:
        hash_val = self.hash_value(key)
        
        if not self.table[hash_val]:
            self.table[hash_val] = [key]
        else:
            self.table[hash_val].append(key)
        
    def remove(self, key: int) -> None:
        hash_val = self.hash_value(key)
        
        if self.table[hash_val]:
            while key in self.table[hash_val]:
                self.table[hash_val].remove(key)
        
    def contains(self, key: int) -> bool:
        hash_val = self.hash_value(key)
        if self.table[hash_val]:
            return key in self.table[hash_val]
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)