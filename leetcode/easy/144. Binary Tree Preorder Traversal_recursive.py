# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Recursive approach
        nodes = []
        
        self.traversal(root, nodes)
        return nodes
        
        
    def traversal(self, root, nodes):
        if root:
            nodes.append(root.val)
            self.traversal(root.left, nodes)
            self.traversal(root.right, nodes)
        
        