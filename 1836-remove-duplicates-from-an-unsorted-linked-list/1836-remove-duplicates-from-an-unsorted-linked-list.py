# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        if not head: return head
        
        counts = defaultdict(bool)
        
        node = head
        
        while node:
            if node.val in counts:
                counts[node.val] = True
                
            else:
                counts[node.val] = False
            node = node.next
                
        new_head = ListNode(-1)
        new_head.next = head
        
        prev, curr = new_head, head
        
        while curr:
            if counts[curr.val]:
                temp = curr.next
                prev.next = temp
                curr.next = None
                curr = temp
                
            else:
                prev = curr
                curr = curr.next
                
        return new_head.next
                