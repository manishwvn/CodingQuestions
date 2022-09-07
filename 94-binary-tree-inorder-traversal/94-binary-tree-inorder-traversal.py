# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        result = []
        stack = []
        curr_node = root
        while curr_node or stack:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
                
            curr_node = stack.pop()
            result.append(curr_node.val)
            curr_node = curr_node.right
            
        return result
        
        