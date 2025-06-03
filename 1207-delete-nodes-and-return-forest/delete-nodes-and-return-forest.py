# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        delete_set = set(to_delete)
        forest = []

        def process_node(node):
            if not node: return None

            node.left = process_node(node.left)
            node.right = process_node(node.right)

            if node.val in delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)

                return None

            return node

        root = process_node(root)

        if root:
            forest.append(root)
        return forest
        