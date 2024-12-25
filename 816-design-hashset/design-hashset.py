class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hash_set = [None] * self.size

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        value = self.hash(key)

        if not self.hash_set[value]:
            self.hash_set[value] = [key]
        else:
            self.hash_set[value].append(key)

    def remove(self, key: int) -> None:
        value = self.hash(key)

        if self.hash_set[value]:
            while key in self.hash_set[value]:
                self.hash_set[value].remove(key)

    def contains(self, key: int) -> bool:
        value = self.hash(key)

        if self.hash_set[value]:
            return key in self.hash_set[value]
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)