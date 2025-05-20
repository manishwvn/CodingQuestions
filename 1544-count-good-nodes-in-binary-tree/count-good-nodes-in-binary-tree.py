# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, maxm):
            nonlocal good_nodes

            if not root:
                return
            
            if root.val >= maxm:
                maxm = root.val
                good_nodes += 1
            
            dfs(root.left, maxm)
            dfs(root.right, maxm)

        if not root:
            return 0

        good_nodes = 0
        maxm = -float('inf')
        dfs(root, maxm)
        return good_nodes
        