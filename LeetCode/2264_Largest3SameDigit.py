class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxGoodInt = 0
        ans = ""
        l = len(num)
        if l<3:
            return ""

        for i in range(1, l-1):
            if num[i] == num[i-1] and num[i] == num[i+1]:
                if int(num[(i-1):(i+1)]) >= maxGoodInt:
                    maxGoodInt = int(num[(i-1):(i+1)])
                    ans = num[(i-1):(i+2)]
                    print(ans)
        
        return ans

# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         ans=[]
#         temp=1
#         for i in range(1,len(num)):
#             if num[i]==num[i-1]:
#                 temp+=1
#                 if temp==3:
#                     ans.append(num[i])
#                     temp=1
#             else:
#                 temp=1
#         if len(ans)==0:
#             return ""
#         return max(ans)*3

# https://leetcode.com/problems/largest-3-same-digit-number-in-string