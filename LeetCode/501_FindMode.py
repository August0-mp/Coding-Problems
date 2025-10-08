# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = {}
        
        def tree_path(node: TreeNode):
            if not node:
                return
            if node.val in cnt:
                cnt[node.val] += 1
            else:
                cnt[node.val] = 1
            tree_path(node.left)
            tree_path(node.right)
            
        tree_path(root)
        m = max(cnt.values())

        return [n for n in cnt if cnt[n] == m]

# https://leetcode.com/problems/find-mode-in-binary-search-tree