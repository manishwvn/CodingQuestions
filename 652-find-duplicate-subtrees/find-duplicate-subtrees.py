# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        subtrees = defaultdict(int)
        result = []

        def preorder(node):
            if not node:
                return "null"

            serialized = ",".join([str(node.val), preorder(node.left), preorder(node.right)])
            
            subtrees[serialized] += 1

            if subtrees[serialized] == 2:
                result.append(node)
            return serialized
                
        preorder(root)
        return result
        