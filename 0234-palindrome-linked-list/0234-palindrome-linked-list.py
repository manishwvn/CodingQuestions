# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def find_mid(head):
            slow, fast = head, head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        def reverse_list(head):

            prev, curr, fast = None, head, head.next

            while fast:
                curr.next = prev
                prev = curr
                curr = fast
                fast = fast.next

            curr.next = prev

            return curr
    
        mid = find_mid(head)
        head2 = reverse_list(mid)

        while head and head2:
            if head.val != head2.val:
                return False

            head = head.next
            head2 = head2.next

        return True                    

        