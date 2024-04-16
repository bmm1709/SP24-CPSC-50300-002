class SinglyLinkedList:
    class _Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, data):
        new_node = self._Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


# Test the Singly Linked List

if __name__ == '__main__':
    ll = SinglyLinkedList()

    ll.add_last(1)
    ll.add_last(2)
    ll.add_last(3)
    ll.display()  # Output: 1 -> 2 -> 3 -> None
