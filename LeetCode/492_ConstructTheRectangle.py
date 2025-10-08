class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # [L,W], L<=W, W-L == min
        ans = []
        for d in range(1,int(sqrt(area))+1):
            if area%d == 0:
               ans = [area//d, d]
        
        return ans
    
# https://leetcode.com/problems/construct-the-rectangle