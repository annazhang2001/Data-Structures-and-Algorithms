class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0 or n == 1:
            return n
    
        dp_1 = 1
        dp_2 = 0
        
        for i in range(n-1):
            dp_i = dp_1 + dp_2
            dp_2 = dp_1
            dp_1 = dp_i
            
        return dp_1
        