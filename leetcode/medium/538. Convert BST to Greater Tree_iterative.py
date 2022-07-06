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
        
        # Iterative
        stack = []
        cur = root
        
        sum = 0
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
                
            cur = stack.pop()
            sum += cur.val
            cur.val = sum
            
            cur = cur.left
        
        return root
            