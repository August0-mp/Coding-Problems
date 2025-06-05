class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        for i in range(h):
            if matrix[i][0]<target and matrix[i][w-1]<target:
                pass
            else:
                for j in range(w):
                    if target==matrix[i][j]:
                        return True
                return False
        return False

# https://leetcode.com/problems/search-a-2d-matrix