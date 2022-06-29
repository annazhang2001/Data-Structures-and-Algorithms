"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        cur = root
        nxt = cur.left if cur else None
        
        # Quit if either is None
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            # Go from left to right
            cur = cur.next
            
            # Finished looping thru the current level
            if not cur:
                cur = nxt
                nxt = nxt.left
        
        return root
            