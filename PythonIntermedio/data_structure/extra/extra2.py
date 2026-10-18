
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        self.head = Node(data, self.head)

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_all(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data)
            if current_node.next is not None:
                result += " -> "
            current_node = current_node.next
        print(result)


ll = LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.print_all()        # 20 -> 10
ll.insert_back(30)
ll.print_all()        # 20 -> 10 -> 30
ll.delete(10)
ll.print_all()        # 20 -> 30
ll.delete(30)
ll.print_all()        # 20