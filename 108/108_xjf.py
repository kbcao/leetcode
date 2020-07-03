# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(l, r):
            if l >= r: return None
            m = l + r >> 1
            node = TreeNode(nums[m])
            node.left = dfs(l, m)
            node.right = dfs(m + 1, r)
            return node
        return dfs(0, len(nums))