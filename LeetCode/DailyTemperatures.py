class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return ans

# https://leetcode.com/problems/daily-temperatures/description/