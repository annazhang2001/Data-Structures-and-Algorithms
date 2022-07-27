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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        int carry = 0;
        ListNode p1 = l1;
        ListNode p2 = l2;
        
        ListNode dummy = new ListNode(-1);
        ListNode p = dummy;
        
        while (p1 != null || p2 != null || carry != 0) {
            int digit = 0;
            int x = (p1 != null) ? p1.val : 0;
            int y = (p2 != null) ? p2.val : 0;
            
            digit = x + y + carry;
            
            carry = (digit >= 10) ? 1 : 0;
            
            p.next = new ListNode(digit%10);
            p = p.next;
            
            p1 = (p1 == null) ? p1 : p1.next;
            p2 = (p2 == null) ? p2 : p2.next;
            
        }
        
        return dummy.next;
        
    }
}