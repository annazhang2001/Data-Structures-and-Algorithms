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
    public ListNode sortList(ListNode head) {
        
        if (head == null || head.next == null) return head;
        
        ListNode mid = getMid(head);
        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        
        return merge(left, right);

    }
    
    
    // Break up the linked list into two
    
    private ListNode getMid(ListNode head) {
        
        ListNode midPrev = null;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            midPrev = (midPrev == null) ? head : midPrev.next;
            fast = fast.next.next;
        }
        
        ListNode mid = midPrev.next;
        midPrev.next = null;
        
        return mid;
        
    }
    
    // Merge two sorted lists
    
    private ListNode merge(ListNode left, ListNode right) {
        
        ListNode dummy = new ListNode(-1);
        ListNode p = dummy;
        
        ListNode p1 = left;
        ListNode p2 = right;
        
        while (p1 != null && p2 != null) {
            
            if (p1.val <= p2.val) {
                p.next = p1;
                p1 = p1.next;
            } else {
                p.next = p2;
                p2 = p2.next;
            }
            
            p = p.next;
            
        }
        
        p.next = (p1 == null) ? p2 : p1;
        
        return dummy.next;
        
    }
}