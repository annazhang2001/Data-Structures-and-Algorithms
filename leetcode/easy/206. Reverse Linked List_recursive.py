# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Base case
        if head is None or head.next is None:
            return head
        
        # Recursion
        last = self.reverseList(self, head.next)
        
        head.next.next = head
        head.next = None
        
        return last
