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
        
        # Base case
        if not root:
            return 0
        else:
            depth1 = self.maxDepth(root.left)
            depth2 = self.maxDepth(root.right)
            
            return (1 + max(depth1, depth2))
        