# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return head
    
        # find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two lists
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        return head