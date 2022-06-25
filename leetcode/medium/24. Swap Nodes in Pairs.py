# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Recursive Approach
        
        # Base case
        if head is None or head.next is None:
            return head
    
        back = self.swapPairs(head.next.next)
        
        first_node = head
        second_node = head.next
        
        second_node.next = first_node
        first_node.next = back
        head = second_node
        
        
        return head