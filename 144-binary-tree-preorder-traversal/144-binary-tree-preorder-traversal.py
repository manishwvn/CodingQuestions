# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def preorder_helper(root, result):
            if root:
                result.append(root.val)
                preorder_helper(root.left, result)
                preorder_helper(root.right, result)
        
        
        if not root:
            return []
        
        result = []
        preorder_helper(root, result)
        return result
        