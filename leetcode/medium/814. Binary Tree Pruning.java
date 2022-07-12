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
    public TreeNode pruneTree(TreeNode root) {
     
        return contains_one(root) ? root : null;
        
    }
    
    public boolean contains_one(TreeNode root){
        
        if (root == null){
            return false;
        }
        
        boolean left = contains_one(root.left);
        boolean right = contains_one(root.right);
        
        if (left == false){
            root.left = null;
        }
        
        if (right == false){
            root.right = null;
        }
        
        return left || right || (root.val == 1);
    }
}
