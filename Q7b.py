class DoublyLinkedList:
    class _Node:
        def __init__(self, data, prev_node=None, next_node=None):
            self.data = data
            self.prev = prev_node
            self.next = next_node

    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, data):
        new_node = self._Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' <-> ' if current.next else ' <-> None\n')
            current = current.next


# Test the Doubly Linked List

if __name__ == '__main__':
    dll = DoublyLinkedList()

    dll.add_last(1)
    dll.add_last(2)
    dll.add_last(3)
    dll.display()  # Output: 1 <-> 2 <-> 3 <-> None
