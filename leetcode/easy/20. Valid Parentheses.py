class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.push(s[i])
            elif s[i] == ']' or s[i] == ')' or s[i] == '}':
                if not self.isSym(stack.peek(),s[i]):
                    return False
                else:
                    stack.pop()

        return stack.is_empty()
          
    
    def isSym(self, left, right):
        if left == '(' and right == ')':
            return True
        elif left == '{' and right == '}':
            return True
        elif left == '[' and right == ']':
            return True
        return False

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