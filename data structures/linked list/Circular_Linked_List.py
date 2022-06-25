class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = Node(data)
            cur.next.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            if cur.next == self.head:
                break
            cur = cur.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head

        # Empty list
        if self.head is None:
            new_node.next = new_node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node   

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next

                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur

                    # Deletion starts from head.next
                    # since we have already considered head
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next
            

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.prepend("GGG")

cllist.remove("D")
cllist.print_list()

        


   
        