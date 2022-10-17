"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten_dfs(self, previous, curr):
        if not curr:
            return previous
        
        curr.prev = previous
        previous.next = curr
        
        temp = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, temp)
        
        
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        #create dummy node with nextnode as head
        dummy = Node(None, None, head, None)
        self.flatten_dfs(dummy, head)
        
        dummy.next.prev = None
        return dummy.next