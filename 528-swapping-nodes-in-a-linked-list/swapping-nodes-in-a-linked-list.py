# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        count = 0
        left, right = None, head
        while curr:
            count += 1

            if count == k:
                left = curr

            if count > k:
                right = right.next

            curr = curr.next

        left.val, right.val = right.val, left.val

        return head
                

        