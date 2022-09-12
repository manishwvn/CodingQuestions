# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, min_depth):
            if not node:
                return min_depth
            
            min_depth += 1
            if not node.left and not node.right:
                return min_depth
            
            if node.left and not node.right:
                return helper(node.left, min_depth)
            if node.right and not node.left:
                return helper(node.right, min_depth)
            left = helper(node.left, min_depth)
            right = helper(node.right, min_depth)
            
            return min(left, right)
        
        
        return helper(root, 0)
        