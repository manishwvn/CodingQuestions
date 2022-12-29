class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(r, c, pos):
            
            if pos == len(word):
                return True
            
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[pos]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                
                if dfs(nr, nc, pos +1):
                    return True
            
            board[r][c] = temp
            
            return False
            
        
        
        
        pos = 0
        for i in range(m):
            for j in range(n):
                if dfs(i, j, pos): return True
                
        return False
        