class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        result = [[None for _ in range(n)] for _ in range(n)]

        val = 1

        top, left = 0, 0
        right, bottom = n - 1, n - 1

        while top <= bottom and left <= right and val <= n ** 2:
            for i in range(left, right + 1):
                result[top][i] = val
                val += 1
            top += 1

            if left <= right:
                for i in range(top, bottom + 1):
                    result[i][right] = val
                    val += 1
                right -= 1

            if top <= bottom and left <= right:
                for i in range(right, left -1 , -1):
                    result[bottom][i] = val
                    val += 1
                bottom -= 1

            if top <= bottom and left <= right:
                for i in range(bottom, top - 1, -1):
                    result[i][left] = val
                    val += 1
                left += 1

        return result
        