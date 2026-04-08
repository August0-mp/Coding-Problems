class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        cost = [matrix[0]]

        if n == 1:
            return matrix[0][0]

        for i in range(1,n):
            cc = []
            cc.append(min(cost[i-1][0], cost[i-1][1])+matrix[i][0])
            
            for j in range(1,n-1):
                cc.append(min(cost[i-1][j-1], cost[i-1][j], cost[i-1][j+1])+matrix[i][j])

            cc.append(min(cost[i-1][n-2], cost[i-1][n-1])+matrix[i][n-1])

            cost.append(cc)
        
        return min(cost[n-1])

# https://leetcode.com/problems/minimum-falling-path-sum/description/