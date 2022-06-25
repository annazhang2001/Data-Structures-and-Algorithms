# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # Two pointers to find the kth node from the end
        
        dummy = ListNode(-1)
        dummy.next = head
        
        slow = head
        fast = dummy
        prev1 = dummy
        prev2 = dummy
        
        for i in range(k):
            prev1 = fast
            fast = fast.next
            
        # prev1 is the previous node to first node to be swapped
        swap1 = fast
        
        # Find the second node
        while fast.next:
            prev2 = slow
            slow = slow.next
            fast = fast.next
        
        # prev2 is the previous node to second node to be swapped
        # Swap values
        swap2 = slow
        
        tmp = swap1.val
        swap1.val = swap2.val
        swap2.val = tmp
        
        return dummy.next
        
        