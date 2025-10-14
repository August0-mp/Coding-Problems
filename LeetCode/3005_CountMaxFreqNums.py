class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        countDict = {}
        seen = set()
        ans, maxFreq = 0, 0

        for n in nums:
            if n in seen:
                countDict[n]+=1
            else:
                seen.add(n)
                countDict[n]=1

            if countDict[n] == maxFreq:
                ans+=maxFreq
            elif countDict[n] > maxFreq:
                maxFreq = countDict[n]
                ans=maxFreq

        return ans

# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         counter = Counter(nums)
#         max_count = 0
#         max_number = 0

#         for k, v in counter.items():
#             if v > max_count:
#                 max_count = v
#                 max_number = 1
#             elif v == max_count:
#                 max_number += 1
#             else:
#                 continue
        
#         return max_count * max_number
    
# https://leetcode.com/problems/count-elements-with-maximum-frequency