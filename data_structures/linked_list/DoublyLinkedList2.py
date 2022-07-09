
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        # If no head
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            # If append as tail
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur

        

    def prepend(self, data):
        
        # If no head
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            cur = self.head
            new_node = Node(data)
            new_node.next = cur
            cur.prev = new_node
            self.head = new_node

    def insert_after(self, key, data):
        cur = self.head
        new_node = Node(data)
        while cur:
            # Found
            if cur.data == key:
                # If the current node is last node
                if cur.next is None:
                    cur.next = new_node
                    new_node.prev = cur
                    return
                else:
                    nxt = cur.next
                    cur.next = new_node
                    new_node.next = nxt
                    nxt.prev = new_node
                    new_node.prev = cur
                    return

            cur = cur.next

    def insert_before(self, key, data):
        cur = self.head
        new_node = Node(data)

        while cur:
            # Found
            if cur.data == key:
                # if cur is head node
                if self.head == cur:
                    new_node.next = cur
                    cur.prev = new_node
                    self.head = new_node
                    return
                
                # Insert before a node that is not head
                else:
                    previous = cur.prev
                    previous.next = new_node
                    new_node.prev = previous
                    new_node.next = cur
                    cur.prev = new_node
                    return

            cur = cur.next

    def delete(self, key):

        cur = self.head

        while cur:
            # If delete head
            if cur.data == key and cur == self.head:

                if cur.next is None:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    nxt.prev = None
                    self.head = nxt

                    # Delete cur
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return 
            elif cur.data == key:

                # if last node
                if cur.next is None:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    nxt = cur.next
                    prev.next = nxt
                    nxt.prev = prev
                    
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return

            cur = cur.next




    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete(1)
dllist.delete(6)
dllist.delete(4)

dllist.delete(3)
dllist.print_list()