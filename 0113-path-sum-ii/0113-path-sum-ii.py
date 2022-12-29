# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #efficient approach - backtraction
        
        def helper(node, currsum, path, target):
            nonlocal res
            
            if not node:
                return 
            
            currsum += node.val
            #action
            path.append(node.val)
            
            print(path.copy())
            if not node.left and not node.right and currsum == target:
                
                res.append(path.copy())
            
            #recursion
            if node.left:
                helper(node.left, currsum, path, target)
                
            if node.right:
                helper(node.right, currsum, path, target)
            
            #backtrack
            path.pop()
        res = []
        helper(root, 0, [], targetSum)
        return res
        