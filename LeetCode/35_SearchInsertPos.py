class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for n in nums:
            if target<=n:
                return i
            i+=1
        return i 

# https://leetcode.com/problems/search-insert-position