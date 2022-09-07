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
        
        global sum_
        sum_ = 0
        curr = 0
        def helper(node, curr):
            global sum_
            if not node:
                return
            
            if not node.left and not node.right:
                sum_ += curr * 10 + node.val
                
            helper(node.left, curr * 10 + node.val)
            helper(node.right, curr * 10 + node.val)
            
        
        helper(root, curr)
        return sum_
        