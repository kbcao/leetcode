/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private int idx;
    public TreeNode recoverFromPreorder(String S) {
        if (S.length() == 0) return null;
        idx = 0;
        TreeNode root = new TreeNode(parseInt(S));
        Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
        stack.push(new Pair<>(root, 0));
        while (!stack.isEmpty()) {
            int depth = 0;
            while (idx < S.length() && S.charAt(idx) == '-') {
                ++idx;
                ++depth;
            }
            if (depth == 0) break;
            TreeNode node = new TreeNode(parseInt(S));
            while (stack.peek().getValue() >= depth) stack.pop();
            TreeNode parent = stack.peek().getKey();
            if (parent.left == null) parent.left = node;
            else parent.right = node;
            stack.push(new Pair<>(node, depth));
        }
        return root;
    }

    private int parseInt(String s) {
        int res = 0;
        while (idx < s.length() && s.charAt(idx) >= '0' && s.charAt(idx) <= '9') {
            res = res * 10 + s.charAt(idx) - '0';
            ++idx;
        }
        return res;
    }
}