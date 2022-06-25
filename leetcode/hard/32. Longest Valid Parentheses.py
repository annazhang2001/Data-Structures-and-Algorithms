class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_length = 0
        stack = Stack()
    
        for i in range(len(s)):
            if s[i] == "(":
                stack.push(i)
            else:
                if (not stack.is_empty()) and s[stack.peek()] == "(":
                    stack.pop()
                    length = (i - stack.peek()) if not stack.is_empty() else (i+1)
                    print(length)
                    if max_length < length:
                        max_length = length
                else:
                    stack.push(i)
                        
        return max_length
    

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