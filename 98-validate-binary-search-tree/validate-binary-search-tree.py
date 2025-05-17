# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            values.append(root.val)

            inorder(root.right)

        inorder(root)
        
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True
        