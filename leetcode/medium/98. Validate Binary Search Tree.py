# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Recursive approach
        return self.valid_helper(root, None, None)
        
    def valid_helper(self, root, min_val, max_val):
        if root is None:
            return True
        
        if min_val != None and root.val <= min_val:
            return False
        if max_val != None and root.val >= max_val:
            return False
        
        return self.valid_helper(root.left, min_val, root.val) and self.valid_helper(root.right, root.val, max_val)
        