class MaxStack(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.s1 == []:
            self.s1.append([x, x])
        else:
            max_value = max(x,self.s1[-1][1])
            self.s1.append([x, max_value])
            

    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1][0]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return self.s1[-1][1]
        
    def popMax(self):
        """
        :rtype: int
        """
        max_value = self.s1[-1][1]
        
        while self.s1:
            if self.s1[-1][0] == max_value:
                self.s1.pop()
                break
            else:
                self.s2.append(self.s1.pop())
        
        # Reconstruct s1
        while self.s2:
            self.push(self.s2[-1][0])
            self.s2.pop()
        
        return max_value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()