# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
    
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        head = ListNode(-1)
        curr = head

        while heap:
            val, i = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next


        return head.next
