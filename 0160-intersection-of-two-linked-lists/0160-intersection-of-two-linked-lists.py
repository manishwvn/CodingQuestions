# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        tempA, tempB = headA, headB
        
        while tempA != tempB:
            if not tempA:
                tempA = headB
                
            else: 
                tempA = tempA.next
                
                
            if not tempB:
                tempB = headA
                
            else:
                tempB = tempB.next
                
        return tempA
                
            