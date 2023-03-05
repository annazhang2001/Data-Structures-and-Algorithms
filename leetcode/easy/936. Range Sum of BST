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
    int sum = 0;
    public int rangeSumBST(TreeNode root, int low, int high) {
        traverse(low, high, root);
        return sum;
    }

    private void traverse(int low, int high, TreeNode root) {
        if (root == null) {
            return;
        }
        traverse(low, high, root.left);
        if (root.val >= low && root.val <= high) {
            sum += root.val;
        }
        traverse(low, high, root.right);

    }
}