# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def __init__(self):
        self.successor = None
        
    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        reverse_head = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        
        return reverse_head
        
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseN(head, right)
        
        head.next = self.reverseBetween(head.next, left-1, right-1)
        
        return head
        
