# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []
        # Traverse the linked list, store value into array
        p = head
        while p:
            nums.append(p.val)
            p = p.next

        res = self.nextGreaterElement(nums)
        
        return res
            

    def nextGreaterElement(self, nums):
        
        res = [0] * len(nums)
        stack = Stack()
        
        for i in range(len(nums)-1, -1, -1):
            while (not stack.is_empty()) and stack.peek() <= nums[i]:
                stack.pop()
            res[i] = 0 if stack.is_empty() else stack.peek()
            
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