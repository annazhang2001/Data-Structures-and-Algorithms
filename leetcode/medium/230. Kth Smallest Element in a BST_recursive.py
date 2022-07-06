# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
               
   
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Recursive
               
        self.rank = 0
        self.res = 0
               
        def traverse(root, k):
            if root is None:
                return
            traverse(root.left, k)
            
            self.rank += 1
            
            if self.rank == k:
                self.res = root.val
                return
            
            traverse(root.right, k)
        
        traverse(root, k)
        return self.res
               
        