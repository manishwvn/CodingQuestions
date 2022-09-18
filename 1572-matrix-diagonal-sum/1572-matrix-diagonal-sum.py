class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            ans += (mat[i][i] + mat[i][-i-1])
        if len(mat)%2 != 0:
            x=len(mat)//2
            ans -= mat[x][x]
        return ans
        