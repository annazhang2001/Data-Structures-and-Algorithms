# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        hash_map = {}
        
        in_length = len(inorder)
        post_length = len(postorder)
        
        # Hash map for constant-time access
        for i in range(in_length):
            hash_map[inorder[i]] = i
        
        def buildTreeHelper(inorder, in_start, in_end, postorder, post_start, post_end):
            # 继续左闭右开
            if post_end <= post_start:
                return
            
            root_val = postorder[post_end-1]
            in_index = hash_map[root_val]
            left_size = in_index - in_start
            
            root = TreeNode(root_val)
            
            root.left = buildTreeHelper(inorder, in_start, in_index, postorder, post_start, post_start + left_size)
            
            root.right = buildTreeHelper(inorder, in_index + 1, in_end, postorder, post_start + left_size, post_end-1)
            
            
            return root
        
        return buildTreeHelper(inorder, 0, in_length, postorder, 0, post_length)
            
            
            
            
            
            
            
            
            
            
            