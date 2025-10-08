class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        ans = []
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = l-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s < 0:
                    j+=1
                elif s > 0:
                    k-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return ans
    
# https://leetcode.com/problems/3sum/