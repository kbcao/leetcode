# 思想是bfs或者dfs，并保留叶子节点的None的信息，然后相应做反序列化
# 我想到的是bfs，参照leetcode的二叉树表示方法，但要注意不能通过2*i+1获取孩子，因为不是完全二叉树


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 如果按照leetcode的定义方式来做，叶子为None时后序节点不会再生成None，用层次遍历做序列化，同样用层次遍历的思想做反序列化
# 在反序列化（建树）的时候，每次拿两个结点作为当前队列头元素的左右结点（可以避免对叶子下的None的考虑）
class Codec:
    def serialize(self, root):
        if root is None: return ''
        res = []
        queue = [root]
        while queue:
            if queue == [None]*len(queue):
                break
            for _ in range(len(queue)):
                res.append(str(queue[0].val) if queue[0] else 'None')
                if queue[0] is not None:
                    queue.append(queue[0].left)
                    queue.append(queue[0].right)
                queue = queue[1:]
        while res[-1] == 'None':
            res.pop()
        return ','.join(res)

    def deserialize(self, data):
        def build(tree_input, idx):
            res = TreeNode(tree_input[0])
            queue = [res]
            idx = 1
            while queue:
                queue[0].left = TreeNode(tree_input[idx]) if idx < len(tree_input) and tree_input[idx] != 'None' else None
                idx += 1
                queue[0].right = TreeNode(tree_input[idx]) if idx < len(tree_input) and tree_input[idx] != 'None' else None
                idx += 1
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue = queue[1:]
            return res
        if data == '':
            return None
        return build(data.split(','), 0)


# test utils
def build_tree(tree_input, i):
    res = TreeNode(tree_input[0])
    queue = [res]
    idx = 1
    while queue:
        queue[0].left = TreeNode(tree_input[idx]) if idx < len(tree_input) and tree_input[idx] else None
        idx += 1
        queue[0].right = TreeNode(tree_input[idx]) if idx < len(tree_input) and tree_input[idx] else None
        idx += 1
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        queue = queue[1:]
    return res

def first_tra(root):
    if root is None:
        return
    first_tra(root.left)
    print(root.val)
    first_tra(root.right)


if __name__ == "__main__":
    codec = Codec()
    tree_input = [5, 2, 3, None, None, 2, 4, 3, 1]
    root = build_tree(tree_input, 0)
    first_tra(codec.deserialize(codec.serialize(root)))
