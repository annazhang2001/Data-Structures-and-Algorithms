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
    int target;
    List<List<Integer>> res = new LinkedList<>();
    
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        
        // Recursive backtracking
        target = targetSum;
        int sum = 0;
        List<Integer> path = new LinkedList<>();
    
        traverse(root, sum, path);
            
        return res;
        
    }
    
    public void traverse(TreeNode node, int sum, List path){
        
        if (node == null){
            return;
        }
        
        path.add(node.val);
        sum += node.val;
        
        if (node.left == null && node.right == null && sum == target){
            res.add(new LinkedList<>(path));
        }
        
        traverse(node.left, sum, path);
        traverse(node.right, sum, path);
            
            
        path.remove(path.size()-1);
        sum -= node.val;
    }
        
}