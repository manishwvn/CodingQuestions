class FileSystem:

    def __init__(self):
        
        self.paths = {}
        

    def createPath(self, path: str, value: int) -> bool:
        
        if len(path) == 0 or path == "/" or path in self.paths:
            return False
        
        last_index = -1
        
        for i in range(len(path) - 1, -1, -1):
            if path[i] == "/":
                last_index = i
                break
                
        if last_index > -1:
            parent_path = path[:last_index]
            
        if len(parent_path) > 1 and parent_path not in self.paths:
            return False
        
        self.paths[path] = value
        return True
    
        

    def get(self, path: str) -> int:
        return self.paths[path] if path in self.paths else -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)