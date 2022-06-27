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
        # Recursive
        levels = []
        
        if root is None:
            return levels
        
        def helper(root, cur_level):
            if len(levels) == cur_level:
                levels.append([])
                
            levels[cur_level].append(root.val)
            if root.left:
                helper(root.left, cur_level + 1)
            if root.right:
                helper(root.right, cur_level + 1)
        
        helper(root, 0)
        return levels
        
        