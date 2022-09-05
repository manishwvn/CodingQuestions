# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder_helper(root, result):
            if not root:
                return
            inorder_helper(root.left, result)
            result.append(root.val)
            inorder_helper(root.right, result)
        
        result = []
        inorder_helper(root, result)
        return result
        
        
        
        
        