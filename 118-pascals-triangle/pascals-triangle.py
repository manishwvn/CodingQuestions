class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)

                else:
                    left = result[i - 1][j - 1]
                    right = result[i - 1][j]
                    row.append(left + right)

            result.append(row)

        return result
