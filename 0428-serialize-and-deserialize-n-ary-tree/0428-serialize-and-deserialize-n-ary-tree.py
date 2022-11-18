"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        
        if not root: return ""
        
        result = []
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        while queue:
            node = queue.popleft()
            
            if not node:
                result.append("#")
                
                if queue: queue.append(None)
                    
            elif node == "C":
                result.append("$")
                
            else:
                result.append(chr(node.val + 48))
                for child in node.children:
                    queue.append(child)
                    
                if queue[0] != None:
                    queue.append("C")
        
        print(result)
        return "".join(result)
        
        
        
	
    def deserialize(self, data: str) -> 'Node':
        
        if not data: return None
        
        root_val = ord(data[0]) - 48
        root = Node(root_val, [])
        
        prev, curr = deque(), deque()
        curr.append(root)
        parent = root
        
        for i in range(1, len(data)):
            
            if data[i] == "#":
                
                prev = curr
                curr = deque()
                
                if prev:
                    parent = prev.popleft()
                    
                else:
                    parent = None
                    
            else:
                if data[i] == "$":
                    parent = prev.popleft() if prev else None
                    
                else:
                    child = Node(ord(data[i]) - 48, [])
                    curr.append(child)
                    parent.children.append(child)
                    
        return root    
                    
                
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))