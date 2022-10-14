"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def clone(node):
            if not node: return None
            if node in hm:
                return hm[node]
            
            new_node = Node(node.val)
            hm[node] = new_node
            return new_node
            
        
        hm = {}
        
        if not head: return None
        
        node = head
        copy_head = clone(head)
        copy_curr = copy_head
        
        while node:
            copy_curr.next = clone(node.next)
            copy_curr.random = clone(node.random)
            node = node.next
            copy_curr = copy_curr.next
            
        return copy_head
            
            
        
        