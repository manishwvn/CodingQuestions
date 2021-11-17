# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        def getIntersect(head):
            p1 = head
            p2 = head
            
            while p2 is not None and p2.next is not None:
                p1 = p1.next
                p2 = p2.next.next
                
                if p1 == p2:
                    return p1
                
            return None
        
        if head is None:
            return None
        
        intersect = getIntersect(head)
        
        if intersect is None:
            return None
        
        p1 = head
        p2 = intersect
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1