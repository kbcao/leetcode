/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    @SuppressWarnings("unchecked")
    public List<TreeNode> generateTrees(int n) {
        if (n < 1) return new ArrayList<TreeNode>();
        ArrayList[][] table= new ArrayList[n + 1][];
        for (int i = 1; i < table.length; ++i) {
            table[i] = new ArrayList[i + 1];
            table[i][i] = new ArrayList<TreeNode>(1);
            table[i][i].add(new TreeNode(i));
        }
        for (int len = 1; len < n; ++len) {
            for (int left = 1; left <= n - len; ++left) {
                int right = left + len;
                List<TreeNode> list = table[right][left] = new ArrayList<>();
                for (TreeNode nr : (List<TreeNode>)table[right][left + 1]) {
                    list.add(new TreeNode(left, null, nr));
                }
                for (int mid = left + 1; mid < right; ++mid) {
                    for (TreeNode nl : (List<TreeNode>)table[mid - 1][left]) {
                        for (TreeNode nr : (List<TreeNode>)table[right][mid + 1]) {
                            list.add(new TreeNode(mid, nl, nr));
                        }
                    }
                }
                for (TreeNode nl : (List<TreeNode>)table[right - 1][left]) {
                    list.add(new TreeNode(right, nl, null));
                }
            }
        }
        return table[n][1];
    }
}