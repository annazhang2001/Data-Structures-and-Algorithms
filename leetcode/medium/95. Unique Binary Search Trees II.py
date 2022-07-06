# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
         
        def buildTree(lo, hi):
            
            
            if lo > hi:
                return [None]
            
            res = []
            for i in range(lo, hi+1):
                
                leftTrees = buildTree(lo, i-1)
                rightTrees = buildTree(i+1, hi)
                
                for l in leftTrees:
                    for r in rightTrees:
                        # Build root
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
        
            return res
            
        return buildTree(1, n)