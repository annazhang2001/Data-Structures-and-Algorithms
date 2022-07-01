# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        # Traversal - backtracking
        self.target = targetSum
        self.curSum = 0
        self.found = False
        
        def traverse(root):
            if root is None:
                return
        
            # preorder
            self.curSum += root.val
            
            # at leaf
            if root.left == root.right:
                if self.curSum == self.target:
                    self.found = True
            
            traverse(root.left)
            traverse(root.right)
            
            # postorder -- backtracked
            self.curSum -= root.val
            
        traverse(root)
        return self.found
        
        