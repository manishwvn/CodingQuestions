# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        if not head: return head
        
        counts = defaultdict(int)
        
        node = head
        while node:
            counts[node.val] += 1
            node = node.next
        
        new_head = ListNode(-1)
        curr_head = new_head
        for i, v in counts.items():
            if v == 1:
                node = ListNode(i)
                curr_head.next = node
                curr_head = curr_head.next
                
        return new_head.next
        