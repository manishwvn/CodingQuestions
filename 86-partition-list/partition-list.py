# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less = []
        greater = []
        curr = head

        while curr:
            if curr.val < x:
                less.append(curr.val)
            else:
                greater.append(curr.val)
            curr = curr.next

        dummy = ListNode()
        curr = dummy

        for num in less:
            num_node = ListNode(num)
            curr.next = num_node
            curr = curr.next

        for num in greater:
            num_node = ListNode(num)
            curr.next = num_node
            curr = curr.next
        
        return dummy.next
        