# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        # Iterative - Stack
        stack = []
        cur = root
        
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                tmp = stack[-1].right
                if tmp:
                    cur = tmp
                else:
                    # Pop
                    tmp = stack.pop()
                    res.append(tmp.val)
                    # Return from right
                    while stack and tmp == stack[-1].right:
                        tmp = stack.pop()
                        res.append(tmp.val)          
            
        return res
            
        
        