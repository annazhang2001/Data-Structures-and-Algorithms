from collections import deque
class MovingAverage(object):

    
    # Circular queue implementation
    
    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = [0] * size
        
        self.window_sum = 0
        self.head = 0
        self.count = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.count += 1
        
        tail = (self.head + 1) % self.size
        
        # Update window sum
    
        self.window_sum = self.window_sum - self.queue[tail] + val
        
        
        # Update val
        self.queue[tail] = val
        # New head
        self.head = (self.head + 1) % self.size
        
        
        return float(self.window_sum) / float(min(self.size, self.count))
        
        
        
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)