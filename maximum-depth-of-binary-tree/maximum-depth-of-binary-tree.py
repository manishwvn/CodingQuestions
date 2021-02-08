# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        depth = 0
        level = [root]
        while level:
            depth += 1
            queue = []
            for ele in level:
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            level = queue
            
        return depth
        