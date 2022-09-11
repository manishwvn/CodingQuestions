# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        
        # middle of LL
        slow, fast = head, head
        
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            
        mid = slow
        
        #reverse from mid
        prev, curr = None, mid.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        
        #two pointer approach
        res = True
        start, end = head, prev
        while start and end:
            if start.val != end.val:
                res = False
            start = start.next
            end = end.next
            
        return res
    
    #T.C. O(n)
    #S.C. O(1)
            
        
        