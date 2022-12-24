# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(leftRoot, rightRoot):
            if not leftRoot and not rightRoot:
                return True

            if leftRoot and rightRoot and leftRoot.val == rightRoot.val:
                return helper(leftRoot.left, rightRoot.right) and helper(leftRoot.right, rightRoot.left)

            return False
    
        return helper(root, root)
        