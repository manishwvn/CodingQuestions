# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, currSum):
        
            if not root:
                return 0

            currSum = currSum * 10 + root.val

            if not root.left and not root.right:
                return currSum

            return helper(root.left, currSum) + helper(root.right, currSum)
    
        return helper(root, 0)
        