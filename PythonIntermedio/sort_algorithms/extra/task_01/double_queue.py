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
            print(current.data, end="")
            if current.next is not None:
                print(" <-> ", end="")
            current = current.next
        print()

    def bubble_sort(self):
        changes_made = True
        while changes_made:
            changes_made = False
            current = self.head
            while current is not None and current.next is not None:
                if current.data > current.next.data:
                    temp= current.data
                    current.data = current.next.data
                    current.next.data = temp
                    changes_made = True
                current= current.next


d = DoubleQueue()
d.push_right(3)
d.push_right(1)
d.push_right(2)
d.push_left(9)
print("Antes:")
d.show_structure()         # 9 3 1 2
d.bubble_sort()
print("Después (valores):")
d.show_structure()         # 1 2 3 9