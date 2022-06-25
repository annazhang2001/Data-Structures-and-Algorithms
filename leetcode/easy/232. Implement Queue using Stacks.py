class MyQueue(object):

    def __init__(self):
        # 队尾
        self.s1 = Stack()
        # 队头
        self.s2 = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.push(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()
        

    def empty(self):
        """
        :rtype: bool
        """
        
        return self.s1.is_empty() and self.s2.is_empty()
        
        

# create Stack class

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def get_list(self):
        return self.items
    
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
    
    def peek(self):
        if self.items != []:
            return self.items[-1]
        else:
            return ''
    
    
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()