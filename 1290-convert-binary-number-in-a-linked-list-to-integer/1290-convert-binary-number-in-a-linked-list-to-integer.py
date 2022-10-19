# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        def getDecimal(num_list):
            result = 0
            j = 0
            for i in range(len(num_list) - 1, -1, -1):
                num = num_list[i]
                result += num * (2 ** j)
                j += 1
                
            return result
                
        
        
        num_list = []
        
        while head:
            num_list.append(head.val)
            head = head.next
            
        
        print(num_list)
        return getDecimal(num_list)
        
        