# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(root):
            nonlocal max_dia
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            max_dia = max(max_dia, left + right)

            return 1 + max(left, right)

        max_dia = 0
        height(root)
        return max_dia
        