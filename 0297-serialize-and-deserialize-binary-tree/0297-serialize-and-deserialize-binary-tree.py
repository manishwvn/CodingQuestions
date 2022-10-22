# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ''
        
        result = ''
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if not node:
                result += 'None,'
                continue
                
            result += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
            
        return result
        

    def deserialize(self, data):
        if not data:
            return None
        
        data_list = data.split(",")
        root = TreeNode(int(data_list[0]))
        queue = deque()
        queue.append(root)
        
        i = 1
        while queue and i < len(data_list):
            node = queue.popleft()
            if data_list[i] != 'None':
                node.left = TreeNode(int(data_list[i]))
                queue.append(node.left)
            i += 1
            if data_list[i] != 'None':
                node.right = TreeNode(int(data_list[i]))
                queue.append(node.right)
            i += 1
            
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))