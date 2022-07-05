# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
    
        def getMin(root):
            while root.left is not None:
                root = root.left
            return root
        
        if root is None:
            return root
        
        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            minNode = getMin(root.right)
            root.right = self.deleteNode(root.right, minNode.val)
            
            minNode.right = root.right
            minNode.left = root.left
            
            root = minNode
            
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            
        return root
            
        
        