# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        # Base case: no tree to be constructed
        if n == 0: return
        
        # Impossible value
        max_index = 0
        
        # Find max index
        for i in range(n):
            if nums[max_index] < nums[i]:
                max_index = i
         
        # Construct root node
        root = TreeNode(nums[max_index])
    
        root.left = self.constructMaximumBinaryTree(nums[0:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1: n])
        
        return root