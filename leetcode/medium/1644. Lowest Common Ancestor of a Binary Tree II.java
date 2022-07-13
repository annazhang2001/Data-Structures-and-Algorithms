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
    
    boolean foundP = false, foundQ = false;
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        TreeNode res = find(root, p, q);
        if (foundP == false || foundQ == false){
            return null;
        }
        
        return res;
        
    }
    
    public TreeNode find(TreeNode root, TreeNode p, TreeNode q){
        
        if (root == null){
            return null;
        }
        
        TreeNode left = find(root.left, p, q);
        TreeNode right = find(root.right, p, q);
        
        if (left != null && right != null){
            return root;
        }
        
        // Found p
        if (root.val == p.val){
            foundP = true;
            return root;
        }
        
        // Found q
        else if (root.val == q.val){
            foundQ = true;
            return root;
        }
        
        return left != null ? left : right;
        
    }
}