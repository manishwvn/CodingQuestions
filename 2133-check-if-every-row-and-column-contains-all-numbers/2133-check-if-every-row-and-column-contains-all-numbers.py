class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        rows, cols = defaultdict(set), defaultdict(set)
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]:
                    return False
                rows[i].add(matrix[i][j])
                cols[j].add(matrix[i][j])
                
        return True