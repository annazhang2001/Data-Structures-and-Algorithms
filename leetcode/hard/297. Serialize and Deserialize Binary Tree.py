from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    # Level-order serial

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        queue = deque()
        queue.append(root)

        res = []
        
        while queue:
            cur = queue.popleft()
            if cur is None:
                res.append("N")
                continue
            
            res.append(str(cur.val))
            
            queue.append(cur.left)
            queue.append(cur.right)
                
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []
        
        nodes = data.split(",")
        length = len(nodes)
        
        root = TreeNode(int(nodes[0]))
        queue = deque()
        queue.append(root)
        i = 1
        
        while i < length:
            
            # 队列存的都是父节点
            parent = queue.popleft()
    
            # 左侧
            if nodes[i] == "N":
                parent.left = None
            else:
                parent.left = TreeNode(int(nodes[i]))
                queue.append(parent.left)
            i += 1
            
            # 右侧
            if nodes[i] == "N":
                parent.right = None
            else:
                parent.right = TreeNode(int(nodes[i]))
                queue.append(parent.right)
        
            i += 1
            
        
        return root
            
        
        
        
        
        
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))