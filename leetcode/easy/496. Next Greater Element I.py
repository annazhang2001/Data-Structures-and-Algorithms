class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        map = {}
        res = self.nextGreaterElementHelper(nums2)
        ans = [0] * len(nums1)
        
        for i in range(len(nums2)):
            map[nums2[i]] = res[i]
    
        
        for j in range(len(nums1)):
            ans[j] = map[nums1[j]]
            
        return ans
        
        
    
    def nextGreaterElementHelper(self, nums):
        stack = Stack()
        res = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            while (not stack.is_empty()) and stack.peek() <= nums[i]:
                stack.pop()
            
            res[i] = -1 if stack.is_empty() else stack.peek()
            stack.push(nums[i])
        
        return res
        
        

# create Stack class

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def get_list(self):
        return self.items
    
    def pop(self):
        self.items.pop()
    
    def push(self, item):
        self.items.append(item)
    
    def peek(self):
        if self.items != []:
            return self.items[-1]
        else:
            return ''
        