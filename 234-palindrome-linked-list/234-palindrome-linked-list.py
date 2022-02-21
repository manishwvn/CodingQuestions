# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head and head.next is None:
            return True
        
        stack = []
        
        node = head
        while node:
            stack.append(node.val)
            node = node.next
            
        node = head
        while stack:
            ele = stack.pop()
            if ele != node.val:
                return False
            
            node = node.next
                
        return True
            
            
        