class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r"/+", "/", path)
        arr = []
      
        for s in path.split("/"):
            if s == ".." and len(arr):
                arr.pop()
            elif len(s) and s != "." and s != ".." :
                arr.append(s)
        return "/" + "/".join(arr)

# https://leetcode.com/problems/simplify-path/