# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def dfs(root, node_list):
            if not root:
                return
            dfs(root.left, node_list)
            node_list.add(root.val)
            dfs(root.right, node_list)
        
        node_list1, node_list2 = set(), set()
        dfs(root1, node_list1)
        dfs(root2, node_list2)

        for num in node_list1:
            if target - num in node_list2:
                return True
        return False


