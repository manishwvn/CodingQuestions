class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        dirs = [[-1,0], [0,-1], [1,0],[0,1]]
        
        def backtrack(r, c, pos):
            #base:
            if pos == len(word):
                return True
            
            if r < 0 or c < 0 or r == m or c == n or board[r][c] == "#":
                return False
            
            #logic
            if board[r][c] == word[pos]:
                #action
                # char = board[r][c]
                board[r][c] = "#"
                
                for dir in dirs:
                    nr, nc = dir[0] + r, dir[1] + c
                    if backtrack(nr, nc, pos + 1):
                        return True
                    
                board[r][c] = word[pos]
            
            return False
        
        
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False 
        