# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def recurrencePath(node):
            ans.append(node.val)

            if node.left:
                recurrencePath(node.left)
            if node.right:
                recurrencePath(node.right)
            return
        if root:
            recurrencePath(root)
        return ans

# https://leetcode.com/problems/binary-tree-preorder-traversal