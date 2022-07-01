# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        self.hashmap = {}
        res = []
        
        def serialize(root):
            
            if root is None:
                return "#"
            
            left = serialize(root.left)
            right = serialize(root.right)
            
            myself = left + "," + right + "," + str(root.val)
            
            freq = self.hashmap.get(myself, 0)
            
            if freq == 1:
                res.append(root)
            
            self.hashmap[myself] = freq + 1
            
            return myself
        
        serialize(root)
        return res
        
        
        
                
                
        
        
        
        
        