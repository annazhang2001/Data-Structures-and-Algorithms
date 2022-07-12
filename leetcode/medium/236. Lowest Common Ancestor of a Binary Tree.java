package leetcode.medium;

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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        return find(root, p, q);
        
    }
    
    public TreeNode find(TreeNode root, TreeNode p, TreeNode q){
        
        if (root == null){
            return null;
        }
        if (root.val == p.val || root.val == q.val){
            return root;
        }
        
        TreeNode left = find(root.left, p, q);
        TreeNode right = find(root.right, p, q);
        
        // Found --> root being the point of division of p and q
        if (left != null && right != null){
            return root;
        }
        
        // At least one of the values is not found
        // If both not found, return null
        return left != null ? left : right;
        
    }
}