# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        hash_map = {}
        pre_length = len(preorder)
        post_length = len(postorder)
        
        # Constant-time access
        for i in range(post_length):
            hash_map[postorder[i]] = i
            
        
        def buildTreeHelper(preorder, pre_start, pre_end, postorder, post_start, post_end):
            # 左闭右闭
            
            if pre_start > pre_end:
                return
            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])
    
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            
            left_root = preorder[pre_start+1]
            index_po = hash_map[left_root]
            left_size = index_po - post_start + 1

            root.left = buildTreeHelper(preorder, pre_start + 1, pre_start + left_size, postorder, post_start, index_po)
                
            root.right = buildTreeHelper(preorder, pre_start + left_size + 1, pre_end, postorder, index_po + 1, post_end - 1)
                
           
        
            return root
        
        return buildTreeHelper(preorder, 0, pre_length-1, postorder, 0, post_length-1)
                
              
        
                
                
        
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        