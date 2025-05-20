# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def inorder(root):
            nonlocal prev, min_dist
            if not root: return

            inorder(root.left)
            if prev:
                min_dist = min(min_dist, root.val - prev.val)

            prev = root

            inorder(root.right)

        prev = None
        min_dist = float('inf')
        inorder(root)
        return min_dist
        