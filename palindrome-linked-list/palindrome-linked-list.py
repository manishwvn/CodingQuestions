# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            
        return prev
    
    def middle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def isPalindrome(self, head: ListNode) -> bool:
        
        fast = head
        slow = self.middle(head)
        slow = self.reverse(slow)
        
        while slow:
            if slow.val != fast.val:
                return False
            
            slow = slow.next
            fast = fast.next
            
        return True
        
        
        