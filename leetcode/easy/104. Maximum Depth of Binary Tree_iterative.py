# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = 0
        self.depth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.res
        
    # Iterative Approach
    def traverse(self, root):
        if root is None:
            return
        else:
            # 进入节点 depth 自加
            self.depth += 1
            
            self.traverse(root.left)
            self.traverse(root.right)
            
            if root.left is None and root.right is None:
                self.res = max(self.depth, self.res)
            
            # 离开节点，depth自减
            self.depth -= 1
            
            
    
        