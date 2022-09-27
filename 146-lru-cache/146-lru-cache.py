class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)

        elif len(self.cache) == self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]
            node = ListNode(key, value)
            self.add(node)
            self.cache[key] = node

        elif len(self.cache) < self.capacity:
            node = ListNode(key, value)
            self.add(node)
            self.cache[key] = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)