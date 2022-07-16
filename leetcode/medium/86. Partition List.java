
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
    public ListNode partition(ListNode head, int x) {
        
        if (head == null){
            return head;
        }
        
        ListNode headS = new ListNode(-500), headL = new ListNode(-500), p = head;
        ListNode Stail = headS, Ltail = headL;
        
        while (p != null){
            if (p.val < x){
                Stail.next = p;
                Stail = Stail.next;
            }
            else {
                Ltail.next = p;
                Ltail = Ltail.next;
            }
            
            p = p.next;
        }
        
        // Attach
        Stail.next = headL.next;
        Ltail.next = null;
        
        return headS.next;
        
    }
}