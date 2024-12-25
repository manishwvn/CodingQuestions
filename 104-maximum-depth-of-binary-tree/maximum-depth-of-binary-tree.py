# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, max_depth):
            if not node:
                return max_depth

            max_depth += 1
            if not node.left and not node.right: return max_depth
            left = dfs(node.left, max_depth)
            right = dfs(node.right, max_depth)
            return max(left, right)

        if not root: return 0
        return dfs(root, 0)
