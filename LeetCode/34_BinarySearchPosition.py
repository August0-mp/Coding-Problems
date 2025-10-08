class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l == 0:
            return [-1, -1]
        i = 0
        j = l - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                left = m
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                right = m
                while right < l - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
        
        return [-1, -1]
    
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/