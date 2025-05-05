"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:

        arr = []

        curr = root

        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr
        