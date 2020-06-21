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
    int res, maxVal;
    public int maxPathSum(TreeNode root) {
        res = maxVal = 0x80000000;
        dfs(root);
        return res > 0 ? res : maxVal;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;
        maxVal = Math.max(maxVal, node.val);
        int lsum = dfs(node.left);
        int rsum = dfs(node.right);
        int sum = Math.max(0, node.val + Math.max(lsum, rsum));
        res = Math.max(res, Math.max(sum, node.val + lsum + rsum));
        return sum;
    }
}