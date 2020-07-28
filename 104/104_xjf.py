# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node == None: return 0
            return max(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)