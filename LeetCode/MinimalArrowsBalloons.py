class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0]) 

        p0 = points[0]
        ans=1

        for p in points[1:]:
            if p0[1]<p[0]:
                ans+=1
                p0=p
            else:
                p0[1] = min(p0[1], p[1])
        return ans
    
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons