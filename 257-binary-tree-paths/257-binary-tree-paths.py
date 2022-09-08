# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def helper(node, path):
            nonlocal result
            
            if not node:
                return
            
            path.append(node.val)
            temp_path = copy.deepcopy(path)
            
            #check for leaf
            if not node.left and not node.right:
                path_str = ""
                for i in range(len(temp_path)):
                    if i == len(path) - 1:
                        path_str += str(temp_path[i])
                        
                    else:
                        path_str += str(temp_path[i]) + "->"
                result.append(path_str)
                    
            
            if node.left:
                helper(node.left, path)
                
            if node.right:
                helper(node.right, path)
                
            path.pop()
        
        # if not root.left and not root.right:
        #     return [str(root.val)]
        result = []
        helper(root, [])
        return result
        