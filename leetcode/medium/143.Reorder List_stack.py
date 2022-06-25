# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        stack = Stack()
        loop_head = head
        list_length = 0
        
        # Push onto stack
        while loop_head:
            stack.push(loop_head)
            loop_head = loop_head.next
            list_length += 1
        
        counter = 0
        cur = head
        while counter < (list_length // 2):
            reorder_node = stack.pop()
                
            tmp = cur.next
            cur.next = reorder_node
            reorder_node.next = tmp
            
            cur = tmp
            if counter == (list_length // 2) - 1:
                tmp.next = None
            
            counter += 1

        return head

# create Stack class

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def get_list(self):
        return self.items
    
    def pop(self):
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
    
    def peek(self):
        if self.items != []:
            return self.items[-1]
        else:
            return None