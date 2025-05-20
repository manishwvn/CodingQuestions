# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        level = 0
        queue.append(root)

        while queue:
            prev = float('inf') if level % 2 != 0 else -float('inf')
            
            for _ in range(len(queue)):
                node = queue.popleft()

                if level % 2 == 0:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                
                else:
                    if node.val % 2 == 1 or node.val >= prev:
                        return False

                prev = node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            level += 1

        return True



        