package leetcode.medium;

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
    public ListNode[] splitListToParts(ListNode head, int k) {
        int N = 0;
        ListNode[] res = new ListNode[k];
        
        ListNode p = head;
        while (p != null){
            N++;
            p = p.next;
        }
        
        int part_length = N / k;
        int rem = N % k;
        int counter;
        
        ListNode cur = head;
        
        for (int i = 0; i < k; i++){
            
            res[i] = cur;
            if (i < rem){
                counter = part_length + 1;
            }
            else {
                counter = part_length;
            }
            
            while (counter-1 > 0){
                if (cur != null){
                    cur = cur.next;
                }
                counter--;
            }
            
            if (cur != null){
                ListNode tmp = cur.next;
                cur.next = null;
                cur = tmp;
            }
            else {
                break;
            }
            
        }
        
        return res;
        
    }
}