import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = sign*x
        revx = 0
        upper = 2147483647
        floor = upper//10
        
        while x != 0:
            tail = x % 10
            x = x // 10
            if (revx > floor) or (revx == floor and tail > 7):
                return 0
            revx = revx*10 + tail
            
        return sign*revx
            
        