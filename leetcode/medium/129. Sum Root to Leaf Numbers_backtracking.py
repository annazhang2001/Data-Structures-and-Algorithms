# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.curSum = 0
        self.sum = 0
        
        # Recursive backtracking
        def traverse(root):
            if root is None:
                return
            
            self.curSum = self.curSum * 10 + root.val
            
            # If leaf
            if root.left == root.right:
                self.sum += self.curSum
                
            traverse(root.left)
            traverse(root.right)
            
            self.curSum = (self.curSum - root.val) / 10
        
        traverse(root)
        return self.sum