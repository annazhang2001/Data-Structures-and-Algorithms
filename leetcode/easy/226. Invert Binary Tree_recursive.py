# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # Recursive / 分解
        if root is None:
            return
        
        right = self.invertTree(root.left)
        left = self.invertTree(root.right)
        
        root.left = left
        root.right = right
        
        return root
        