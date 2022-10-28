# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def helper(node, currSum):
            nonlocal count
            
            if not node:
                return 
            
            currSum += node.val
            
            if currSum == k:
                count += 1
                
            count += hm[currSum - k]
            
            #action
            hm[currSum] += 1
            
            #recurse
            helper(node.left, currSum)
            helper(node.right, currSum)
            
            #backtrack
            hm[currSum] -= 1
        
        
        count, k = 0, targetSum
        hm = defaultdict(int)
        helper(root, 0)
        return count
        