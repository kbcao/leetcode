# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(node, value):
            if node == None: return False
            value += node.val
            if value == sum and node.left == None and node.right == None: return True
            return dfs(node.left, value) or dfs(node.right, value)
        return dfs(root, 0)