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
        
        # Recursive dp; num at this level
        def dfs(cur, num):
            if cur is None:
                return 0
            
            num = num * 10 + cur.val
            if cur.left == cur.right:
                return num
            
            return dfs(cur.left, num) + dfs(cur.right, num)
            
        return dfs(root, 0)
            
            
        