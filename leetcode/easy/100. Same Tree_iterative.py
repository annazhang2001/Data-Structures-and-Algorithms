from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Iterative - BFS
        
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
     
        deq = deque([(p,q)],)
        while deq:
            p, q = deq.popleft()
            
    
            if not check(p,q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True
        
        