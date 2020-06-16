/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode node =  q.poll();
            sb.append(node == null ? "null" : node.val);
            sb.append(',');
            if (node == null) continue;
            q.offer(node.left);
            q.offer(node.right);
        }
        sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] vals = data.split(",");
        if (vals.length == 0) return null;
        TreeNode root = createTreeNode(vals[0]);
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        for (int i = 1; i < vals.length; i += 2) {
            while (q.peek() == null) q.poll();
            TreeNode node =  q.poll();
            node.left = createTreeNode(vals[i]);
            node.right = createTreeNode(vals[i + 1]);
            q.offer(node.left);
            q.offer(node.right);
        }
        return root;
    }

    private TreeNode createTreeNode(String s) {
        try { return new TreeNode(Integer.parseInt(s)); }
        catch (Exception ignored) {}
        return null;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));