# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
    
        # 非stack, extra space O(1)解法
        # Edge case: if only one head
        if head.next is None:
            return head
        
        # Find middle point of linked list
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        
        # Detach
        slow.next = None
        
        # reverse from mid
        prev = None
        curr = mid
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        reverse_head = prev
        
        # Merge two linked lists
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        
        p1 = head
        p2 = reverse_head
        
        while p1:
            if p1:
                p.next = p1
                p1 = p1.next
                p = p.next
            
            if p2:
                p.next = p2
                p2 = p2.next
                p = p.next
            
    
        return dummy.next
            
        
        
        
        
        
        
        
        
        