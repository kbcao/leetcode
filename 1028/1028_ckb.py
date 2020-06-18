# 维护一个栈，往下走的时候入栈，回退的时候出栈
# 看当前的这个节点的深度，如果确定是下一层的，就直接作为栈顶的左孩子
# 如果不是下一层的，就一直出栈，回退到这个结点所在的层，然后把结点作为栈顶的右孩子（可以想象成右边的叶子）

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path= []
        pos= 0
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]
