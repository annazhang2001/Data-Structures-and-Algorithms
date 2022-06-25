from collections import deque 

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        max_nums = []
        queue = MonotonicQueue()
        
        # 框架
        for i in range(len(nums)):
            if i < (k-1):
                queue.push(nums[i])
            else:
                queue.push(nums[i])
                max_nums.append(queue.max())
                queue.pop(nums[i-k+1])
            
        return max_nums
            
            
        
        

        
# Implement a monotonic queue (from left to right)
class MonotonicQueue():
    
    def __init__(self):
        self.queue = deque()
    
    def max(self):
        # The last one is the max
        return self.queue[-1]
    
    def push(self, num):
        while (len(self.queue) > 0 and self.queue[0] < num):
            self.queue.popleft()
        self.queue.appendleft(num)
    
    def pop(self, n):
        if self.queue[-1] == n:
            self.queue.pop()
    
    
    
        