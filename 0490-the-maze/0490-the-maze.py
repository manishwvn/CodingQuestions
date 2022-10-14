class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        m, n = len(maze), len(maze[0])
        
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        queue = deque()
        queue.append(start)
        
        row, col = start
        maze[row][col] = 2
        
        while queue:
            r, c = queue.popleft()
            if r == destination[0] and c == destination[1]:
                return True
            
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                
                while (nr >= 0 and nc >= 0) and (nr < m and nc < n) and maze[nr][nc] != 1:
                    nr, nc = nr + dir[0], nc + dir[1]
                    
                print(nr , nc)
                if maze[nr - dir[0]][nc - dir[1]] != 2:
                    queue.append([nr - dir[0], nc - dir[1]])
                    maze[nr - dir[0]][nc - dir[1]] = 2
                    
        return False
                    
            
        
        
        