# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev = None
    
        def helper(root):
            nonlocal prev
            if not root:
                return True

            if not helper(root.left):
                return False

            if prev and prev.val >= root.val:
                return False

            prev = root
            if not helper(root.right):
                return False

            return True

        return helper(root)
        