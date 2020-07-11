struct Node {
    int val, smaller, cnt, lazy;
    Node *left, *right;
    Node(int val, int smaller) : val(val), smaller(smaller),
        cnt(1), lazy(0), left(nullptr), right(nullptr) {}

};

struct Tree {
    Node *root;
    Tree(int val) { root = new Node(val, 0); }
    int insert(int val) {
        int smaller = 0;
        Node *node = root;
        while (true) {
            // 先处理一下懒加载
            if (node->lazy > 0) {
                node->smaller += node->lazy;
                if (node->left != nullptr) {
                    node->left->lazy += node->lazy;
                }
                if (node->right != nullptr) {
                    node->right->lazy += node->lazy;
                }
                node->lazy = 0;
            }

            // 如果目标值大则向右走
            if (val > node->val) {
                smaller = node->smaller + node->cnt;
                if (node->right == nullptr) {
                    node->right = new Node(val, smaller);
                    return smaller;
                }
                else node = node->right;
            }
            // 如果目标值小则向左走
            else if (val < node->val) {
                ++node->smaller;
                if (node->right != nullptr) {
                    ++node->right->lazy;
                }
                if (node->left == nullptr) {
                    node->left = new Node(val, smaller);
                    return smaller;
                }
                else node = node->left;
            }
            // 如果目标值相等直接返回
            else {
                ++node->cnt;
                if (node->right != nullptr) {
                    ++node->right->lazy;
                }
                return node->smaller;
            }
        }
    }
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> counts(nums.size());
        if (nums.size() == 0) return counts;
        *counts.rbegin() = 0;
        Tree tree(*nums.rbegin());
        for (int i = nums.size() - 2; i >= 0; --i) {
            counts[i] = tree.insert(nums[i]);
        }
        return counts;
    }
};