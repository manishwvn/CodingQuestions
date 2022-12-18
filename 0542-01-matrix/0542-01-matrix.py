class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        distances = [[float('inf') for _ in range(n)] for _ in range(m)]
    
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                else:
                    if i > 0:
                        distances[i][j] = min(distances[i][j], distances[i-1][j] + 1)
                    if j > 0:
                        distances[i][j] = min(distances[i][j], distances[i][j-1] + 1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1:
                    distances[i][j] = min(distances[i][j], distances[i+1][j] + 1)
                if j < n-1:
                    distances[i][j] = min(distances[i][j], distances[i][j+1] + 1)

        return distances



