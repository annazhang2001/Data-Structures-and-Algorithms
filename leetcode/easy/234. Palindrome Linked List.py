# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        if fast != None:
            slow = slow.next
        
        left = head
        right = self.reverseList(slow)
        
        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
                
        return True
    
    def reverseList(self, head):
        pre = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        return pre
        
    