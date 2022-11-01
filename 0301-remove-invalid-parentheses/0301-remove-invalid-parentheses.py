class Solution:
    def isValid(self, string):
        count = 0
        for char in string:
            if char.isalpha(): continue
                
            if char == "(": count += 1
            if char == ")": count -= 1
                
            if count < 0: return False
            
        return count == 0
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        if not s or len(s) == 0: return []
        
        result = []
        
        queue = deque()
        visited = set()
        queue.append(s)
        visited.add(s)
        flag = False
        
        while queue and not flag:
            size = len(queue)
            
            for i in range(size):
                string = queue.popleft()
                if self.isValid(string):
                    result.append(string)
                    flag = True
                    
                if not flag:
                    for j in range(len(string)):
                        if string[j].isalpha():
                            continue
                            
                        child = string[:j] + string[j+1:]
                        if child not in visited:
                            queue.append(child)
                            visited.add(child)
                            
        return [""] if not result else result
        