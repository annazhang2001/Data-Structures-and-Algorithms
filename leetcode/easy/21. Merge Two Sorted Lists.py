# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        p1 = list1
        p2 = list2
        
        # Dummy pointer
        dummy = ListNode(-1)
        p = dummy
        
        while p1 != None and p2 != None:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next  
            p = p.next
            
        # Take care of remaining linked lists
        if p1 != None:
            p.next = p1
        if p2 != None:
            p.next = p2
        
        return dummy.next
                
            
                