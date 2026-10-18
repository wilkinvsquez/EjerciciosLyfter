class Node:
    data: str
    next: "Node"

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Queue(): 
    head: Node

    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            return None

        data = self.head.data
        self.head = self.head.next
        return data


    def print_all(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += current_node.data
            if current_node.next is not None:
                result += " -> "
            current_node = current_node.next
        print(result)

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()
print(q.dequeue())
q.print_all() 