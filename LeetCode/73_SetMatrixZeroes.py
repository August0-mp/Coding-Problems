class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        def mapZeros() -> List[List[int]]:
            zeros = []
            for i in range(h):
                for j in range(w):
                    if matrix[i][j]==0:
                        zeros.append([i,j])
            return zeros
        
        for p in mapZeros():
            for i in range(h):
                matrix[i][p[1]]=0
            for i in range(w):
                matrix[p[0]][i]=0
            
# https://leetcode.com/problems/set-matrix-zeroes/