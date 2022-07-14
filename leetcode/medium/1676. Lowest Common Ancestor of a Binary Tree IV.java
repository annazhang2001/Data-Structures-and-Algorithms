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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        HashSet<Integer> hash = new HashSet<>();
        for (TreeNode node : nodes){
            hash.add(node.val);
        }
        
        return find(root, hash);
    }
    
    public TreeNode find(TreeNode root, HashSet hash){
        if (root == null){
            return null;
        }
        
        if (hash.contains(root.val)){
            return root;
        }
        
        TreeNode left = find(root.left, hash);
        TreeNode right = find(root.right, hash);
        
        if (left != null && right != null){
            return root;
        }
        
        return left != null? left : right;
    }
}