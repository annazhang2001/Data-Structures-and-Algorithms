class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        
        # Initialize an zero array
        arr = [0 for i in range(length)]
        df = Difference(arr)
        
        for update in updates:
            df.increment(update[0], update[1], update[2])
        
        return df.result()

class Difference:
    
    def __init__(self, arr):
        self.df = []
        self.df.append(arr[0])
        
        # Diff array
        for i in range(1, len(arr)):
            self.df.append(arr[i] - arr[i-1])
        
        self.length = len(self.df)
        
        
    
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
        
        
        
        
        
        
        
        