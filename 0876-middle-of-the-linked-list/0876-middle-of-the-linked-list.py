# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        return slow
            
            
        