# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        sorted_arr = []
        
        def inorder(root):
            
            if not root:
                return 
            
            inorder(root.left)
            sorted_arr.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        left, right = 0, len(sorted_arr)
        
        def helper(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            value = sorted_arr[mid]
            node = TreeNode(value)
            
            node.left = helper(start, mid-1)
            node.right = helper(mid +1, end)
            return node
        
        return helper(0, len(sorted_arr) - 1)
            
            
            
        