# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
    
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            size = len(queue)
            result.append(queue[-1].val)
            for i in range(size):
               
                
                node = queue.popleft()
                print(node.val, end = ' ')
                    

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()


        return result


