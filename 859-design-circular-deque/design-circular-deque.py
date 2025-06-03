class ListNode:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.left = ListNode(0)  # Dummy head
        self.right = ListNode(0)  # Dummy tail
        self.left.next = self.right
        self.right.prev = self.left

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = ListNode(value, self.left.next, self.left)
        self.left.next.prev = node
        self.left.next = node
        self.size -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = node
        self.right.prev = node
        self.size -= 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.right.prev = self.right.prev.prev
        self.right.prev.next = self.right
        self.size += 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.size == 0