# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def arrayToBST(array, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    node = TreeNode(array[mid]) 
    
    if start == end:
        return node
    
    node.left = arrayToBST(array, start, mid - 1)
    node.right = arrayToBST(array, mid + 1, end)
    
    return node
    
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        array = []
        while head:
            array.append(head.val)
            head = head.next
            
        return arrayToBST(array, 0, len(array) - 1)
    