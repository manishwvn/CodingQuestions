# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        if not node:
            return []
        
        if not node.left and not node.right:
            return [[node.val]]
        
        level = 1
        queue1, queue2 = collections.deque(), collections.deque()
        queue1.append((node))
        result = []
        
        while queue1 or queue2:
            temp = []
            if level % 2 != 0:
                size = len(queue1)
                for _ in range(size):
                    node = queue1.popleft()
                    temp.append(node.val)
                    
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)
                        
                level += 1
                
            else:
                size = len(queue2)
                for _ in range(size):
                    node = queue2.pop()
                    temp.append(node.val)
                    
                    
                    if node.right:
                        queue1.appendleft(node.right)
                    if node.left:
                        queue1.appendleft(node.left)
                        
                level += 1
            
            result.append(temp)
            
        return result
                        
                    
                    
        
        