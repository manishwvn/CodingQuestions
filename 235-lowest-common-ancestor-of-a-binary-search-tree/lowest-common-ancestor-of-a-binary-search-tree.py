# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # if not root:
        #     return None

        # if p == root or q == root:
        #     return root

        # elif p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)

        # return root

        def dfs(root):
            nonlocal lca

            if not root:
                return
            
            lca = root
            if root == p and root == q:
                return

            elif p.val < root.val and q.val < root.val:
                dfs(root.left)

            elif p.val > root.val and q.val > root.val:
                dfs(root.right)
            
            else:
                return

        lca = root
        dfs(root)
        return lca