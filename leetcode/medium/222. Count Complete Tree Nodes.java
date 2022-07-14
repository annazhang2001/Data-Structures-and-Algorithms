package leetcode.medium;

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
    public int countNodes(TreeNode root) {
        int hl = 0;
        int hr = 0;
        
        TreeNode left = root, right = root;
        
        while (left != null){
            hl++;
            left = left.left;
        }
        
        while (right != null){
            hr++;
            right = right.right;
        }
        
        if (hl == hr){
            return (int) Math.pow(2, hl) - 1;
        }
        
        else {
            return 1 + countNodes(root.left) + countNodes(root.right);
        }
        
    }
}