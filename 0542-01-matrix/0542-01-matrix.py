class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])
                    
                else:
                    mat[i][j] = -1
                    
        while queue:
            r, c = queue.popleft()
            
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    
                    queue.append([nr, nc])
                    
        return mat
        
        