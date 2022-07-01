# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        hash_map = {}
        pre_length = len(preorder)
        in_length = len(inorder)
        
        # Quick easy access
        for i in range(in_length):
            hash_map[inorder[i]] = i
            
        def buildTreeHelper(preorder, pre_start, pre_end, inorder, in_start, in_end):
            
            # 左闭右开
            if pre_start >= pre_end:
                return

            root_val = preorder[pre_start]
            in_index = hash_map[root_val]
            left_size = in_index - in_start
            
            root = TreeNode(root_val)
            root.left = buildTreeHelper(preorder, 1 + pre_start, pre_start + left_size + 1, inorder, in_start, in_index)
            
            root.right = buildTreeHelper(preorder, pre_start + left_size + 1, pre_end, inorder, in_index + 1, in_end)
            
            return root
        
        return buildTreeHelper(preorder, 0, pre_length, inorder, 0, in_length)
    
        