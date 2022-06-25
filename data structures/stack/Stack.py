class Stack:
    def __init__(self):
        self.items = []
    def pop(self):
        self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return self.items == []
    
    def get_stack(self):
        return self.items
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.get_stack()

stack.pop()
stack.get_stack()