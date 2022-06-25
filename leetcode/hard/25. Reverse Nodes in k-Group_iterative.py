# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # Iterative solution
        
        a = head
        b = head
        prev = None
        
        # Count k nodes
        for i in range(k):
            if b is None:
                return head
            b = b.next
        
        reversed_head = self.reverse(a,b)
        head = reversed_head
        
        # connect
        prev = a
        a.next = b
        # jump
        a = b
        
        # move forward
        while a:
            # Count k nodes
            for i in range(k):
                if b is None:
                    return head
                b = b.next
            
            prev.next = self.reverse(a,b)
            prev = a
            a.next = b
            a = b
        
        
        return head
        
        
    
    def reverse(self, a, b):
        
        # Iterative reversal everything from a to b (exclusive)
        next = None
        prev = None
        cur = a
        
        while cur != b:
            next = cur.next
            
            cur.next = prev
            prev = cur
            cur = next
        
        return prev