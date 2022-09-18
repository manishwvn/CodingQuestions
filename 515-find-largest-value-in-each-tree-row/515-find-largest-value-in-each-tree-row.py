# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        #bfs
        queue = collections.deque()
        queue.append(root)
        result = []
        
        while queue:
            # temp = []
            max_val = None
            size = len(queue)
            # for i in range(size):
            #     temp.append(queue[i].val)
                
            # max_val = max(temp)
            # result.append(max_val)
            
            for _ in range(size):
                node = queue.popleft()
                
                if max_val == None or node.val >= max_val:
                    max_val = node.val
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(max_val)
                    
        return result
            
        
        
        