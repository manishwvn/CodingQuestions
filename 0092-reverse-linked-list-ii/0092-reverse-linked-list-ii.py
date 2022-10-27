# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        new_head = ListNode(0, head)
        
        left_prev, curr = new_head, head
        
        for i in range(left-1):
            left_prev, curr = curr, curr.next
        
        #reverse the links
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        #update pointers
        left_prev.next.next = curr
        left_prev.next = prev
        
        return new_head.next
            