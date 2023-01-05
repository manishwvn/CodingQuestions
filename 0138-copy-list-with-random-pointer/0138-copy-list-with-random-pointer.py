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
        
        #O(2.n) TC
        #O(n) SC
        
        if not head: return None
        
        
        copy_head = Node(head.val)
        hm = {head:copy_head}
        
        node = head
        copy_node = copy_head
        
        while node.next:
            node = node.next
            new_node = Node(node.val)
            copy_node.next = new_node
            copy_node = copy_node.next
            hm[node] = copy_node
        
        node, copy_node = head, copy_head
        
        while node and copy_node:
            if node.random:
                copy_node.random = hm[node.random]
                
            node = node.next
            copy_node = copy_node.next
            
        return copy_head
        
        