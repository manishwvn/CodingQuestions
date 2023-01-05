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
        
        def create_copy(node):
            if not node: return None
            
            if node in hm:
                return hm[node]
            new_node = Node(node.val)
            hm[node] = new_node
            return new_node
        
        if not head: return None
        
        hm = {}
        copy_head = create_copy(head)
        node, copy_node = head, copy_head
        
        while node:
            copy_node.next = create_copy(node.next)
            copy_node.random = create_copy(node.random)
            node, copy_node = node.next, copy_node.next
        
        # for k, v in hm.items():
        #     print(k.val, v.val)
        
        return copy_head
            
        
        
        
        
        
        
        