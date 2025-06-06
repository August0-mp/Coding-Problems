class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        min_row, max_row = 0, n - 1
        min_col, max_col = 0, n - 1
        count = 1

        while count <= n * n:
            # Move right
            for j in range(min_col, max_col + 1):
                matrix[min_row][j] = count
                count += 1
            min_row += 1

            # Move down
            for i in range(min_row, max_row + 1):
                matrix[i][max_col] = count
                count += 1
            max_col -= 1

            # Move left
            for j in range(max_col, min_col - 1, -1):
                matrix[max_row][j] = count
                count += 1
            max_row -= 1

            # Move up
            for i in range(max_row, min_row - 1, -1):
                matrix[i][min_col] = count
                count += 1
            min_col += 1

        return matrix
    
# https://leetcode.com/problems/spiral-matrix-ii