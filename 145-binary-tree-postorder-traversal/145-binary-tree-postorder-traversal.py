# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def postorder_helper(root, result):
            if root:
                postorder_helper(root.left, result)
                postorder_helper(root.right, result)
                result.append(root.val)
        
        
        if not root:
            return []
        
        result = []
        postorder_helper(root, result)
        return result
        