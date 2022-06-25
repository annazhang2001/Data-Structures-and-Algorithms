# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        dummy = ListNode(-1)
        dummy.next = head
        
        # prev node
        p = dummy
        
        slow = head
        fast = head
        
        for i in range(n):
            # Let fast go
            fast = fast.next
        
        while fast:
            p = slow
            slow = slow.next
            fast = fast.next
        
        p.next = slow.next
        slow.next = None
        
        return dummy.next
        
        
        
        
        