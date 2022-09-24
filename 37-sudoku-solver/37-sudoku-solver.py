class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        rowset, colset, boxset = [defaultdict(int) for i in range(9)], [defaultdict(
        int) for i in range(9)], [defaultdict(int) for i in range(9)]

        def get_box_idx(r, c):
            return (r//3)*3 + c//3

        def is_valid(r, c, val):
            return not (rowset[r][val] or colset[c][val] or boxset[get_box_idx(r, c)][val])

        def helper(r, c):

            if c == n:
                r, c = r+1, 0

            if r == n:
                return True

            if board[r][c] != '.':
                return helper(r, c+1)

            for val in range(1, n+1):
                if is_valid(r, c, val):
                    rowset[r][val] = colset[c][val] = boxset[get_box_idx(
                        r, c)][val] = 1
                    board[r][c] = str(val)
                    if helper(r, c+1):
                        return True
                    rowset[r][val] = colset[c][val] = boxset[get_box_idx(
                        r, c)][val] = 0
                    board[r][c] = '.'

            return False
        
        
        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    val = int(board[r][c])
                    rowset[r][val] = colset[c][val] = boxset[get_box_idx(
                        r, c)][val] = 1
                
        helper(0, 0)