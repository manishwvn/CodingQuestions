# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        p1, p2 = head, head
        
        for i in range(n):
            
            if p2.next == None:
                
                if i == n - 1:
                    head = head.next
                return head
            
            p2 = p2.next
            
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        
        p1.next = p1.next.next
        
        return head
        
        
        