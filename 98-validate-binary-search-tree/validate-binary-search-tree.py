# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(root):
            nonlocal prev

            if not root:
                return True
            
            if not inorder(root.left):
                return False
            
            if root.val <= prev:
                return False

            prev = root.val
            return inorder(root.right)
            

        prev = -float("inf")
        return inorder(root)
        