# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        
        def helper(root):
            if not root: return -1
            
            leftH = helper(root.left)
            rightH = helper(root.right)
            
            maxH = max(leftH, rightH) + 1
            
            if maxH == len(result):
                result.append([])
                
            result[maxH].append(root.val)
            
            return maxH
            
        helper(root)
        
        return result
        