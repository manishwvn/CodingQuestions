class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        dirs = [[1,0], [-1,0], [0,1],[0,-1]]
        
        queue = []
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    
                else:
                    mat[i][j] = -1
                    
                    
        while queue:
            row, col = queue.pop(0)
            
            for i in range(len(dirs)):
                rowPrime = row + dirs[i][0]
                colPrime = col + dirs[i][1]
                
                if rowPrime >= 0 and colPrime >= 0 and rowPrime < len(mat) and colPrime < len(mat[0]) and mat[rowPrime][colPrime] < 0:
                    queue.append((rowPrime, colPrime))
                    mat[rowPrime][colPrime] = mat[row][col] + 1
                    
                    
        return mat 
        
        