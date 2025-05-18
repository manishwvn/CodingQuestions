# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False
            
            return same_tree(p.left, q.left) and same_tree(p.right, q.right)



        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        #case 1 same tree
        if root.val == subRoot.val:
            if same_tree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        