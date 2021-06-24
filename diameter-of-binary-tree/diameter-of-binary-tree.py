# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        all_heights = self.get_all_heights(root)
        all_heights[None] = 0
        
        return self.get_diameter_opt(root, all_heights)
        # return self.get_diameter(root)
    
    def get_diameter_opt(self, node: TreeNode, all_heights: dict) -> int:
        if node is None:
            return 0
        return max(all_heights[node.left] + all_heights[node.right], self.get_diameter_opt(node.left, all_heights), self.get_diameter_opt(node.right, all_heights))
        
        
    def get_all_heights(self, root: TreeNode) -> dict:
        all_heights = {} 
        if root.left is not None:
            all_heights.update(self.get_all_heights(root.left))
        if root.right is not None:
            all_heights.update(self.get_all_heights(root.right))
        
        heights = [0]
        if root.left is not None:
            heights.append(all_heights[root.left])
        if root.right is not None:
            heights.append(all_heights[root.right])
            
        all_heights[root] = 1+ max(heights)
        
        return all_heights
    
    
    
    
    def get_diameter(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return max(self.get_height(node.left) + self.get_height(node.right), self.get_diameter(node.left), self.get_diameter(node.right))
    
    def get_height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))