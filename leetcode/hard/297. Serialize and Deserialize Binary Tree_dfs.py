# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    # Preorder serial

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        res = []

        def serial(root):
            
            if root is None:
                res.append('N')
                return
            
            res.append(str(root.val))
                
            serial(root.left)
            serial(root.right)
        
        serial(root)
        
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        vals = data.split(",")
        self.index = 0
        
        def deser(vals):
            if vals[self.index] == 'N':
                self.index += 1
                return None
            node = TreeNode(int(vals[self.index]))
            self.index += 1
            node.left = deser(vals)
            node.right = deser(vals)
        
            return node
        
        return deser(vals)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))