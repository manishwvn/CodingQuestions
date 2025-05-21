# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        def dfs(node):
            nonlocal nodes
            if not node:
                return None
            
            if node in nodes:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            else:
                return left or right

        nodes = set(nodes)
        return dfs(root)
