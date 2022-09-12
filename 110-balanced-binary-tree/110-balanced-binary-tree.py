# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
                
        def helper(node):
            if not node:
                  return True, 0
                
            left, left_height = helper(node.left)
            if not left:
                return False, 0
            
            right, right_height = helper(node.right)
            if not right:
                return False, 0
            
            return (abs(left_height - right_height) <2), max(left_height, right_height) + 1
            
        check, height = helper(root)
        return check
        