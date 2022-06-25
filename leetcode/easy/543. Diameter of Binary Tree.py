# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxD = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDiameter(root)
        return self.maxD
        
    def maxDiameter(self, root):
        if root is None:
            return 0
        
        leftMax = self.maxDiameter(root.left)
        rightMax = self.maxDiameter(root.right)
        
        maxD_sub = leftMax + rightMax
        self.maxD = max(maxD_sub, self.maxD)
        
        return 1 + max(leftMax, rightMax)