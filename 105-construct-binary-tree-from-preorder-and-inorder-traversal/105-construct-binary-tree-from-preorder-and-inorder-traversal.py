# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        global idx, index_map
        idx = 0
        index_map = {}
        for i, v in enumerate(inorder):
            index_map[v] = i
            
        def helper(left, right):
            global idx, index_map
            if left > right:
                return None
            
            node_val = preorder[idx]
            node = TreeNode(node_val)
            
            idx += 1
            
            node.left = helper(left, index_map[node_val] - 1)
            node.right = helper(index_map[node_val] + 1, right)
            return node
            
        return helper(0, len(preorder) - 1)