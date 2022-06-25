# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode 
        """
        
        # 非首尾相连做法
        pA = headA
        pB = headB
        
        # Find lengths
        lenA = 0
        lenB = 0
        
        while pA:
            pA = pA.next
            lenA += 1
        
        while pB:
            pB = pB.next
            lenB += 1
        
        pA = headA
        pB = headB
        if lenA >= lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            for i in range(lenB - lenA):
                pB = pB.next
          
        while pA and pB:
            if pA == pB: return pA
            pA = pA.next
            pB = pB.next
        
        return pA
            
        
       