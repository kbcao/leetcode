# 想到的是中序遍历是回文，但是有许多坑：
# 1. 叶子节点下的None和有一个孩子的结点的None要区分
# 2. 为了防止不同的树出现同样的中序遍历结果，需要每次在root结点的左右加上当前递归的mark
# 3. 返回遍历结果时需要用数组，否则负数无法判断回文

# 但是其实可以用递归做，更简单，直接看左右子树根是否相等，然后递归判断
# l子树的l孩子和r子树的r孩子
# l子树的r孩子和r子树的l孩子
# 是否是对称即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def get_bfs(root,cnt):
            if root is None:
                return ['X']
            if root.left is None and root.right is None:
                return [str(root.val)]
            left=get_bfs(root.left,cnt+1)
            mid=str(root.val)
            right=get_bfs(root.right,cnt+1)
            return left+[str(cnt),mid,str(cnt)]+right
        bfs=get_bfs(root,1)
        print(bfs)
        return bfs==bfs[::-1]


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def fun(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val==right.val and fun(left.left,right.right) and fun(left.right,right.left)
        return True if root is None else fun(root.left,root.right)


if __name__ == "__main__":
    s = Solution()
    print(s.isSymmetric(38))
