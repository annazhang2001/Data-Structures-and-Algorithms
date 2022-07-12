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
    public List<Integer> rightSideView(TreeNode root) {
        
        // Level-order traversal
        Deque<TreeNode> queue = new ArrayDeque<>();
        LinkedList<Integer> res = new LinkedList<>();
        
        if (root == null){
            return res;
        }
        
        queue.addLast(root);
        
        while (!queue.isEmpty()){
            int size = queue.size();
            
            for (int i = 0; i < size; i++){
                TreeNode cur = queue.remove();
                if (i == (size - 1)){
                    res.addLast(cur.val);
                }
                if (cur.left != null){
                    queue.addLast(cur.left);
                }
                if (cur.right != null){
                    queue.addLast(cur.right);
                }
            }
            
            
        }
        
        return res;
        
    }
}