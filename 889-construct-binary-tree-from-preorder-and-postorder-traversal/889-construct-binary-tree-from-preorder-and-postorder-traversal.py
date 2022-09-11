# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    
        idx={}
        for i,j in enumerate(pre):
            idx[j]=i
        def helper(start,end,post):

            if end==start:
                return None

            if end-start==1:
                return TreeNode(post.pop())


            node=TreeNode(post.pop()) #3
            ind=idx[post[-1]] #4

            node.right=helper(ind,end,post) #1
            node.left=helper(start+1,ind,post) #2
            return node

        return helper(0,len(pre),post)
