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
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        
        // edge case
        if (head == null) {
            return head;
        }
        
        int length = 0;
        ListNode tail = head;
        ListNode dummy = new ListNode(-101);
        dummy.next = head;
        
        while (tail.next != null) {
            length++;
            tail = tail.next;
        }
        
        length++;
        int rotate = k % length;
        int inv = length - rotate;
        
        ListNode p = head;
        
        for (int i = 0; i < inv; i++) {
            tail.next = p;
            
            p = p.next;
            tail.next.next = null;
            tail = tail.next;
            
            dummy.next = p;
            
        }
        
        return dummy.next;
        
    }
}