# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, max_depth):
            if not node:
                return max_depth
            
            max_depth += 1
            if not node.left and not node.right:
                return max_depth
            
            left = helper(node.left, max_depth)
            right = helper(node.right, max_depth)
            
            return max(left, right)
        
        
        return helper(root, 0)
        