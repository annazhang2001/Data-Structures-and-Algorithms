package leetcode.easy;
import java.util.LinkedList;
import java.util.List;
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
    LinkedList<String> path = new LinkedList<>();
    LinkedList<String> res = new LinkedList<>();
    
    public List<String> binaryTreePaths(TreeNode root) {
        
        // Backtracking
        
        construct_path(root);
        return res;
    }
    
    public void construct_path(TreeNode root){
        if (root == null){
            return;
        }
        
        if (root.left == null && root.right == null){
            path.addLast(root.val + "");
            res.addLast(String.join("->", path));
            path.removeLast();
            return;
        }
        
        path.addLast(root.val + "");
        construct_path(root.left);
        construct_path(root.right);
        path.removeLast();
    }
}