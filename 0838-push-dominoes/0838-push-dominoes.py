class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dom = list(dominoes)
        queue = deque()
        
        for i, d in enumerate(dom):
            if d != ".":
                queue.append((i, d))
                
        while queue:
            i, d = queue.popleft()
            
            if d == "L":
                if i > 0 and dom[i-1] == ".":
                    queue.append((i-1, "L"))
                    dom[i-1] = "L"
                    
                    
            if d == "R":
                if i + 1 < len(dom) and dom[i+1] == ".":
                    if i + 2 < len(dom) and dom[i+2] == "L":
                        queue.popleft()
                        
                    else:
                        queue.append((i+1, "R"))
                        dom[i+1] = "R"
                        
        return "".join(dom)
                        
                    
                
        
        
        