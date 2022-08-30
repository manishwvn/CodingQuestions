class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        if not mat or not mat[0]:
            return []
        
        m = len(mat)
        n = len(mat[0])
        r = 0
        c = 0
        dir = 1
        i = 0
        result = [0 for i in range(m * n)]
        
        while i < m*n:
            result[i] = mat[r][c]
            i += 1
            
            #direction up
            if dir == 1:
                if c == n - 1:
                    r += 1
                    dir = -1
                elif r == 0:
                    c += 1
                    dir = -1
                else:
                    r -= 1
                    c += 1
            #direction down
            else:
                if r == m - 1:
                    c += 1
                    dir = 1
                elif c == 0:
                    r += 1
                    dir = 1
                else:
                    c -= 1
                    r += 1
        
        return result
                    
                
                
        
            
        