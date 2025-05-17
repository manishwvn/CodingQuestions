# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right: return root.val

        depth = 0
        sum_ = 0
        stack = [(root, 0)]

        while stack:
            node, curr = stack.pop()

            if not node.left and not node.right:
                if depth < curr:
                    depth = curr
                    sum_ = node.val

                elif depth == curr:
                    sum_ += node.val

            
            else:
                if node.right:
                    stack.append((node.right, curr + 1))

                if node.left:
                    stack.append((node.left, curr + 1))

        return sum_

        