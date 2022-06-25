import Queue as queue

class MyStack(object):

    def __init__(self):
        self.q = queue.Queue()
        self.top_elem = None
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.put(x)
        self.top_elem = x
        

    def pop(self):
        """
        :rtype: int
        """
        size = self.q.qsize()
        while size > 2:
            self.q.put(self.q.get())
            size -= 1
        
        # when size == 2
        new_top = self.q.get()
        self.top_elem = new_top
        self.q.put(new_top)
        
        return self.q.get()

    def top(self):
        """
        :rtype: int
        """
        return self.top_elem

    def empty(self):
        """
        :rtype: bool
        """
        
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()