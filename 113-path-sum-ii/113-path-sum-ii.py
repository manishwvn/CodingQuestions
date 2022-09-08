# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def helper(node, currsum, path, target):
            nonlocal res
            
            if not node:
                return 
            
            currsum += node.val
            path.append(node.val)
            
            if not node.left and not node.right and currsum == target:
                res.append(path)
                
            if node.left:
                helper(node.left, currsum, deepcopy(path), target)
                
            if node.right:
                helper(node.right, currsum, deepcopy(path), target)
            
        
        res = []
        helper(root, 0, [], targetSum)
        return res
        