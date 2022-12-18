# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root
        

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        
        self.root = self.stack.pop()
        val = self.root.val
        self.root = self.root.right
        
        return val
        

    def hasNext(self) -> bool:
        return self.root or self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()