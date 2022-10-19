# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        num = head.val
        while head.next:
            next_val = head.next.val
            num = num * 2 + next_val
            head = head.next
            
        return num
            
            
        