/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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

    ListNode head;
    
    
    public TreeNode sortedListToBST(ListNode head) {
        
        this.head = head;
        int size = findSize(head);
        
        return convertListToBST(0, size-1);
        
        
    }
    private TreeNode convertListToBST(int l, int r) {
        if (l > r) {
            return null;
        }
        
        
        int mid = (l + r) / 2;
        
        TreeNode left = convertListToBST(l, mid - 1);
        
        TreeNode node = new TreeNode(this.head.val);
        this.head = this.head.next;
        
        node.left = left;
        
        TreeNode right = convertListToBST(mid + 1, r);
        
        node.right = right;
        
        return node;
        
    }
    
    
    private int findSize(ListNode head) {
        int size = 0;
        ListNode cur = head;
        while (cur != null) {
            size++;
            cur = cur.next;
        }
        
        return size;  
    }
    
    
    
}