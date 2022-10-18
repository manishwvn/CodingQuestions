# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        if head.next and not head.next.next:
            return head
        
        t1 = head
        t2 = head.next
        even_head = t2
        
        while t2 and t2.next:
            t1.next = t2.next
            t1 = t1.next
            t2.next = t1.next
            t2 = t2.next
            
        t1.next = even_head
        return head
        
            
        