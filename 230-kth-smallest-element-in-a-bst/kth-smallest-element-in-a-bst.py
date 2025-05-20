# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):
            nonlocal result, k

            if not root:
                return
            
            inorder(root.left)
            k -= 1
            if k == 0:
                result = root.val
                return
                
            inorder(root.right)

        result = None
        inorder(root)
        return result

        