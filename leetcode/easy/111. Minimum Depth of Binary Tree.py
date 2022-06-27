from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Iterative; Queue; BFS
        
        if root is None:
            return 0
        
        minDep = sys.maxint
        queue = deque()
        queue.append(root)
        level = 0
        
        while queue:
            level += 1
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                # Reached leaf
                if node.left is None and node.right is None:
                    return level
        
            
            
            
            
    
        
        
        