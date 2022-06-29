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
        
        # Iterative (greedier)
        if not root:
            return None
        
        node = root
        while node:
            
            # If the node has a left child
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            
            # Move on to the right side of the tree
            node = node.right
        
        