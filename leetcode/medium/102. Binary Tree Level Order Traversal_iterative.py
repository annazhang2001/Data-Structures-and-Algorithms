from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Iteration
        levels = []
        
        
        # Empty root
        if root is None:
            return levels
        
        level = 0
        queue = deque([root])
        
        while queue:
            # Number of elements in current level
            level_length = len(queue)
            levels.append([])
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level += 1
        
        return levels
              