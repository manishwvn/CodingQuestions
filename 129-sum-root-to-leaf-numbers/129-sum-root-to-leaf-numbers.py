# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        sum_, curr = 0, 0
        stack = []
        node = root
        
        while node or stack:
            while node:
                curr = curr * 10 + node.val
                stack.append([node, curr])
                node = node.left
                
            node, curr = stack.pop()
            if not node.left and not node.right:
                sum_ += curr
                
            node = node.right
            
        return sum_