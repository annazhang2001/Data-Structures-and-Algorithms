class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        ans = [-1] * n
        
        for i in range(2*n-1):
            
            while stack and nums[i%n] > nums[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = (i%n)
                
            stack.append(i%n)
        
        for i in range(n):
            if res[i] != -1:
                ans[i] = nums[res[i]]
        return ans
        
        
