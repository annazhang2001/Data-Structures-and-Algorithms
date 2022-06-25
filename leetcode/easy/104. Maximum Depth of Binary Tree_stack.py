# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Iteration Using Stack
        stack = []
        
        if root is not None:
            stack.append([1, root])
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(current_depth, depth)
                stack.append([current_depth + 1, root.left])
                stack.append([current_depth + 1, root.right])
            
            
        return depth
        
      