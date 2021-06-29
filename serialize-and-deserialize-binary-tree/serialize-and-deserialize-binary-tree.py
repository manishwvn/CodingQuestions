# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        
        def serializeHelper(root, string):
            
            if root is None:
                string += 'None,'
                
            
            else:
                string += str(root.val) + ','
                string = serializeHelper(root.left, string)
                string = serializeHelper(root.right, string)
            return string
        
        return serializeHelper(root, '')
        

    def deserialize(self, data):
        
        def deserializeHelper(dataList):
            
            if dataList[0] == 'None':
                dataList.pop(0)
                return None
            
            root = TreeNode(dataList[0])
            dataList.pop(0)
            root.left = deserializeHelper(dataList)
            root.right = deserializeHelper(dataList)
            return root
            
            
        dataList = data.split(',')
        root = deserializeHelper(dataList)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))