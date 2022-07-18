package leetcode.easy;

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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        
        if (root1 == null || root2 == null){
            return root1 != null ? root1 : root2;
        }
        
        // Iterative
        Stack<TreeNode[]> stack = new Stack<>();
        stack.push(new TreeNode[]{root1, root2});
        
        while (!stack.isEmpty()){
            TreeNode[] ts = stack.pop();
            
            if (ts[0] == null || ts[1] == null){
                continue;
            }
            
            ts[0].val += ts[1].val;
            
            if (ts[0].left == null){
                ts[0].left = ts[1].left;
            }
            else {
                stack.push(new TreeNode[]{ts[0].left, ts[1].left});
            }
            
            if (ts[0].right == null){
                ts[0].right = ts[1].right;
            }
            else {
                stack.push(new TreeNode[]{ts[0].right, ts[1].right});
            }
            
        }
        
        return root1;
        
        
        
    }
        
}