# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return True

            nonlocal result

            left = dfs(node.left)
            right = dfs(node.right)

            if not left and not right:
                return False

            if node.left and node.val != node.left.val:
                return False

            if node.right and node.val != node.right.val:
                return False

            if left and right:
                result += 1
                return True
            return False
        result = 0
        dfs(root)
        return result