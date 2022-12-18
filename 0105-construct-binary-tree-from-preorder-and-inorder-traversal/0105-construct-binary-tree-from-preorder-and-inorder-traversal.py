# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        hm = {}
    
        for i, val in enumerate(inorder):
            hm[val] = i
    
        def helper(preorder, preStart, preEnd, inorder, inStart, inEnd, hm):
            if preStart > preEnd or inStart > inEnd:
                return None

            rootVal = preorder[preStart]
            root = TreeNode(rootVal)
            index = hm[rootVal]

            root.left = helper(preorder, preStart+1, preStart+index-inStart, inorder, inStart, index-1, hm)
            root.right = helper(preorder, preStart+index-inStart+1, preEnd, inorder, index+1, inEnd, hm)

            return root

        return helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, hm)
        