# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Change into linked list
        left = root.left
        right = root.right
    
        root.left = None
        root.right = left
    
        p = root
        
        while p.right:
            p = p.right
        
        p.right = right
        
        
        
        