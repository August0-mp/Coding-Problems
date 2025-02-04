class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def parenthesisAux(s: str, popen: int, pclose: int):
            if(popen == pclose and popen+pclose==2*n):
                ans.append(s)
                return 

            if(popen < n):
                parenthesisAux(s+"(",popen+1,pclose)
                
            if(pclose < popen):
                parenthesisAux(s+")",popen,pclose+1)
            
        parenthesisAux("",0,0)
        return ans

# https://leetcode.com/problems/generate-parentheses/