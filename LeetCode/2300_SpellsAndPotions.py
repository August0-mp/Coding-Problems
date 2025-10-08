class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []

        lp = len(potions)
        ls = len(spells)

        potions.sort()

        for i in range(ls):
            left = 0
            right = lp-1
            if spells[i]*potions[0]>=success:
                ans.append(lp)
            elif spells[i]*potions[right]<success:
                ans.append(0)
            else:
                index = -1
                while left<=right:
                    mid = left+(right-left)//2
                    if potions[mid]*spells[i] >= success:
                        index = mid
                        right = mid-1
                    else:
                        left= mid+1
                ans.append(lp-index)

        return ans
    
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions