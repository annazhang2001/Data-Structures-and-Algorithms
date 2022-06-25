from DoublyLinkedList import DoublyLinkedList

class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        return self.items.tail_node()

    def enqueue(self, value):
        return self.items.insert_tail(value)
    
    def dequeue(self):
        return self.items.remove_head()

    def size(self):
        return self.items.length


if __name__ == "__main__" :
    queue_obj = MyQueue()

    print("is_empty(): " + str(queue_obj.is_empty()))
    print("rear(): " + str(queue_obj.rear()))
    print("front(): " + str(queue_obj.front()))
    print("size(): " + str(queue_obj.size()))