class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #bfs approach
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        m, n = len(heights), len(heights[0])
        pac_set, at_set = set(), set()
        result = []
        pac_queue, at_queue = deque(), deque()
        
        def bfs(queue, ocean):
            while queue:
                r, c = queue.popleft()
                ocean.add((r, c))
                
                for dir in dirs:
                    nr, nc = r + dir[0], c + dir[1]
                    if (nr >=0 and nr < m) and (nc >= 0 and nc < n) and (nr, nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                        queue.append((nr, nc))
            
        
        
        for r in range(m):
            pac_queue.append([r, 0])
            at_queue.append([r, n-1])
            
        for c in range(n):
            pac_queue.append([0, c])
            at_queue.append([m-1, c])
            
        bfs(pac_queue, pac_set)
        bfs(at_queue, at_set)
        
        print(pac_set, at_set)
        
        for r in range(m):
            for c in range(n):
                if (r, c) in pac_set and (r, c) in at_set:
                    result.append([r, c])
                    
        return result
        
        