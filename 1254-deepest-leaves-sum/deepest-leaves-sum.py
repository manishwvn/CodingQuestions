# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        if not root.left and not root.right: return root.val

        queue = deque([root])

        while queue:
            curr = queue
            queue = deque()

            for node in curr:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not queue:
                break

        result = 0
        for node in curr:
            result += node.val

        return result
        