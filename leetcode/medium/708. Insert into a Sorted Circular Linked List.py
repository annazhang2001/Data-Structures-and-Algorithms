"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal)
		# If the linked list is empty
        if head is None:
            
            head = new_node
            head.next = head
            
        else:
            prev = head
            cur = head.next
            while prev.next != head:
                if insertVal >= prev.val and insertVal <= cur.val:
                    break
                elif prev.val > cur.val and insertVal <= cur.val:
                    break
                elif prev.val > cur.val and insertVal >= prev.val:
                    break
                prev = cur
                cur = cur.next
            prev.next = new_node
            new_node.next = cur
                
        return head