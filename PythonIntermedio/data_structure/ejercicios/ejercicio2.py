class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleQueue: 
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = removed.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return removed.data
    
    def pop_right(self):
        if self.tail is None:
            return None
        removed = self.tail
        self.tail = removed.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return removed.data


    def show_structure(self):
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()



d = DoubleQueue()
d.push_left(1)
d.push_right(2)
d.push_left(0)
d.show_structure()      # 0 1 2
print(d.pop_right())    # 2
print(d.pop_left())     # 0
print(d.pop_left())     # 1
print(d.pop_left())     # None
d.push_right(5)
d.show_structure()      # 5