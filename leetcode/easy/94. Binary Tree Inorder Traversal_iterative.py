# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Stack - iterative
        
        res = []
        stack = []
        cur = root
        
        while cur or stack:
            # Go left
            while cur:
                stack.append(cur)
                cur = cur.left
            # Inorder append
            cur = stack.pop()
            res.append(cur.val)
            
            cur = cur.right
        
        return res
        