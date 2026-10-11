class Node:
    data: str
    next: "Node"

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class StackPile: 
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        removed = self.top
        self.top = self.top.next
        return removed.data


    def show_structure(self):
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next

pila = StackPile()
print("Add Pushes to stack")
pila.push(10)
pila.push(20)
pila.push(30)
pila.show_structure()   # 30, 20, 10
print("remove last")
print(pila.pop())
print("Left list")     # 30
pila.show_structure()   # 20, 10
print("remove")
pila.pop()
print("remove")
pila.pop()
print(pila.pop())       # None (pila vacía)