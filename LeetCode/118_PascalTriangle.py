class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        def pascalTriangle(i: int):
            if i >= numRows-1:
                return
            row = [1]
            for j in range(i):
                row.append(ans[-1][j]+ans[-1][j+1])
            row.append(1)
            ans.append(row)
            print(row)
            i+=1
            pascalTriangle(i)
        pascalTriangle(1)
        return ans

# https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2025-08-01
