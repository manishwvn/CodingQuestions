class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def hash_key(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash_key(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_key(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = self.hash_key(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)