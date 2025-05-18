class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            if not left or not right:
                return False

            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False

            result += 1
            return True

        dfs(root)
        return result