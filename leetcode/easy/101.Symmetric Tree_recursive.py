from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        
        # Iterative - BFS
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            
            if t1 is None and t2 is None:
                continue
            if (t1 is None and t2 is not None) or (t1 is not None and t2 is None):
                return False
            
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        
        
        return True