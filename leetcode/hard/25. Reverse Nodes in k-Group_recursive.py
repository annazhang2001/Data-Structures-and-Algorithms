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
        
        # Recursive solution
        # Base case: if we have < k nodes
        b = head
        a = head
        
        for i in range(k):
            if b is None: # Do not flip
                return head
            b = b.next
        
        # Reverse [a, b)
        reversed_head = self.reverse(a,b)
        back = self.reverseKGroup(b,k)
        
        a.next = back
        
        return reversed_head
    
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
        
        
    
        