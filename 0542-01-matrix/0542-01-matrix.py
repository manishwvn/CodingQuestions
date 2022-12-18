class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(mat), len(mat[0])

        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = float('inf')

        while queue:
            r, c = queue.popleft()

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr,nc))


        return mat
        