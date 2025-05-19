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
            node_list.append(root.val)
            dfs(root.right, node_list)
        
        node_list1, node_list2 = [], []
        dfs(root1, node_list1)
        dfs(root2, node_list2)

        l, r = 0, len(node_list2) - 1

        while l < len(node_list1) and r > -1:
            if node_list1[l] + node_list2[r] == target:
                return True

            elif node_list1[l] + node_list2[r] < target:
                l += 1
            
            else:
                r -= 1
        return False

    