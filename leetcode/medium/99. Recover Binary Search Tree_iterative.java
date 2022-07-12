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
    TreeNode x = null, y = null, pred = null;
    
    public void swap(TreeNode a, TreeNode b){
        int tmp = a.val;
        a.val = b.val;
        b.val = tmp;
    }
    
    public void findTwoSwapped(TreeNode root){
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode cur = root;
        
        // Traverse
        while (!stack.isEmpty() || cur != null){
            while (cur != null){
                stack.add(cur);
                cur = cur.left;
            }
            
            cur = stack.removeLast();
            if (pred != null && cur.val < pred.val){
                y = cur;
                if (x == null){
                    x = pred;
                }
                else {
                    return;
                }
            }
            
            pred = cur;
            cur = cur.right;
        }
        
    }
    
    public void recoverTree(TreeNode root) {
        
        // Iterative
        
        findTwoSwapped(root);
        swap(x, y);
        
    }
}