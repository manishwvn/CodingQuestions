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
        
        if not head:
            return None
        
        #create mutated list
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
            
        #create random pointers
        curr = head
        copy_curr = curr.next
        
        while curr:
            if curr.random:
                copy_curr.random = curr.random.next
            curr = curr.next.next
            if copy_curr.next:
                copy_curr = copy_curr.next.next
                
        #split the list
        curr = head
        copy_head = curr.next
        copy_curr = copy_head
        
        while curr:
            curr.next = curr.next.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next
            curr = curr.next
            copy_curr = copy_curr.next
            
        return copy_head
        