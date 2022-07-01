# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Recursion
    
        def maxDepth(root):
            # Calculate max depth
            if root is None:
                return 0, True
        
            left, isBalanced_left = maxDepth(root.left)
            right, isBalanced_right = maxDepth(root.right)
            
            isBalanced = isBalanced_left and isBalanced_right
            
            if abs(left - right) > 1:
                isBalanced = False
            
            return 1 + max(left, right), isBalanced
            
        max_Depth, isBalanced = maxDepth(root)
       
        return isBalanced