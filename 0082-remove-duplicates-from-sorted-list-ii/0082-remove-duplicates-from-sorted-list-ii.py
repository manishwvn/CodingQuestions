# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head: return None
        
        new_head = ListNode(-1)
        new_head.next = head
        prev = new_head
        curr = head
        
        while curr:
            
            if curr.next and curr.val == curr.next.val:
                
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                
                prev.next = curr.next
            
            else:
                prev = prev.next
                
            curr = curr.next
            
        return new_head.next
        
        
        