# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # Recursive
        
        self.sum = 0
        
        def sum(root):
            if root is None:
                return
            
            sum(root.right)
            self.sum += root.val
            root.val = self.sum
            
            sum(root.left)
        
        sum(root)
        return root
            
        