class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # Based on the constraint
        length = 1001
        df = Difference(length)
        
        for trip in trips:
            passenger = trip[0]
            start = trip[1]
            end = trip[2]
            df.increment(start, end, passenger)
        
        result = df.result()
        for i in range(length):
            if result[i] > capacity:
                return False
        
        return True

class Difference():
    def __init__(self, length):
        self.length = length
        self.df = [0] * length
    
    def increment(self, start, end, inc):
        self.df[start] += inc
        if end < (self.length - 1):
            self.df[end] -= inc
    
    def result(self):
        res = []
        res.append(self.df[0])
        for i in range(1, self.length):
            res.append(res[i-1]+self.df[i])
        return res