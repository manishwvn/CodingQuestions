# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def checkIfBalanced(root):
    if not root:
        return True, -1
    
    leftBalanced, leftHeight = checkIfBalanced(root.left)
    
    if not leftBalanced:
        return False, 0
    
    rightBalanced, rightHeight = checkIfBalanced(root.right)
    
    if not rightBalanced:
        return False, 0
    
    currentHeight = abs(leftHeight - rightHeight) 
    
    return (currentHeight < 2), 1 + max(leftHeight, rightHeight)
    
    
    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balanced, height = checkIfBalanced(root)
        return balanced
        
    
        