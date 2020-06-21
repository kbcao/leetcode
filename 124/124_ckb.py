# 想到的是建立图，变成邻接表，然后做，肯定很烦

# 没想到用递归做，因为是任意一个结点到任意一个结点，所以递归的时候，同步更新一个 最大值 为 当前值+左(若>0)+右(若>0)
# 但递归返回的时候返回的是 当前值+左 or 当前值+右 的较大者，因为路径不能出现分叉

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res=-0x7fffffff
        def get_max(root):
            nonlocal res
            if root is None:
                return 0
            left=max(get_max(root.left),0)
            right=max(get_max(root.right),0)
            res=max(res,left+right+root.val)
            return root.val+max(left,right)
        _=get_max(root)
        return res
