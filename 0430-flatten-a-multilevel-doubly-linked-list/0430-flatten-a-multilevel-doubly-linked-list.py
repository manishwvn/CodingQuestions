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
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        stack = []
        dummy = head
        
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
                
            if not head.next and stack:
                head.next = stack.pop()
                head.next.prev = head
            
            head = head.next
            
        return dummy
            
              
        