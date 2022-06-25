# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Dummy node that is guaranteed the smallest
        dummy = ListNode(-5001)
        dummy.next = head
        
        prev = head
        cur = head.next
        
        while cur:
            # We should sort
            if cur.val < prev.val:
                
                tmp = dummy
                while cur.val > tmp.next.val:
                    tmp = tmp.next
                prev.next = cur.next
                cur.next = tmp.next
                tmp.next = cur
                
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        
        return dummy.next
                
                
                
                
        