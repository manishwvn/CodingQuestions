# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, result):

            if node:
                dfs(node.left, result)
                dfs(node.right, result)
                result.append(node.val)
    
        if not root:
            return []
        
        result = []
        dfs(root, result)
        return result

        
        