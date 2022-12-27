# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    nodes = {0: [], 1: [TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if n not in Solution.nodes:
            temp = []
            for i in range(n):
                j = n - 1 - i

                for leftNode in self.allPossibleFBT(i):
                    for rightNode in self.allPossibleFBT(j):
                        root = TreeNode(0)
                        root.left = leftNode
                        root.right = rightNode
                        temp.append(root)

            Solution.nodes[n] = temp
                        
                        
        
        
        return Solution.nodes[n]
        
        
        
        
        
        
        
        
        
        