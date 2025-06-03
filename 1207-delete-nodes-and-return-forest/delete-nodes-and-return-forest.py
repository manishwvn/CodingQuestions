# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        if not root:
            return []

        delete_set = set(to_delete)
        forest = []

        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)

                if curr.left.val in delete_set:
                    curr.left = None

            if curr.right:
                queue.append(curr.right)
                if curr.right.val in delete_set:
                    curr.right = None

            if curr.val in delete_set:
                if curr.left:
                    forest.append(curr.left)
                if curr.right:
                    forest.append(curr.right)

        if root.val not in delete_set:
            forest.append(root)

        return forest
        