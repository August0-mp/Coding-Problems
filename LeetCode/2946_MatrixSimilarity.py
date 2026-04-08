class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        if k%n == 0:
            return True
        
        for i in range(0,m,2):
            for j in range(n):
                if mat[i][j] != mat[i][(j+(n-k))%n]:
                    return False
        for i in range(1,m,2):
            for j in range(n):
                if mat[i][j] != mat[i][(j+k)%n]:
                    return False
        
        return True

# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts