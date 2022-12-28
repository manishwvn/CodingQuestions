# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        
        def helper(node):
            if not node: return 0
            
            left = helper(node.left)
            right = helper(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1 : return -1
            return max(left, right) + 1
            
            
        return helper(root) != -1