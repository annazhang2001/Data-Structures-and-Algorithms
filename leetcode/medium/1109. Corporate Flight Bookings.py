class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
        # Initialize an empty array
        arr = [0] * n
        df = Difference(arr)
        
        for booking in bookings:
            df.increment(booking[0]-1, booking[1]-1, booking[2])
            
        return df.result()

# Difference array
class Difference():
    
    def __init__(self, arr):
        self.df = []
        self.df.append(arr[0])
        self.length = len(arr)
        
        for i in range(1, self.length):
            self.df.append(arr[i] - arr[i-1])
        
    
    def increment(self, start, end, inc):
        self.df[start] += inc
        
        if end < (self.length - 1):
            self.df[end+1] -= inc
    
    def result(self):
        res = []
        res.append(self.df[0])
        
        for i in range(1, self.length):
            res.append(res[i-1] + self.df[i])
        
        return res
        
 
        