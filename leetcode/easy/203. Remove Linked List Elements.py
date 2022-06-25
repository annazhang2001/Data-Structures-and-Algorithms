# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                # Remove
                prev.next = curr.next
                curr = curr.next
            else:
                # Just roll on
                prev = curr
                curr = curr.next
            
        return dummy.next