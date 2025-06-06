class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]
        total = 0
        if m==1 or n==1:
            return 1
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                matrix[i][j]=matrix[i+1][j]+matrix[i][j+1]
                total+=matrix[i][j]

        return matrix[0][0]

# https://leetcode.com/problems/unique-paths