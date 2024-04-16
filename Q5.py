class SinglyList:
 class _Node:
 def __init__(self, e, next_node):
 self._element = e
 self._next = next_node

 def __init__(self):
 self._head = self._tail = None

 def add_last(self, e):
 new_node = self._Node(e, None)
 if self._head is None:
 self._head = new_node
 else:
 self._tail._next = new_node
 self._tail = new_node

 def find_median(self):
 if self._head is None:
 return None

 slow_ptr = fast_ptr = self._head
 prev_ptr = None

 while fast_ptr and fast_ptr._next:
 prev_ptr = slow_ptr
 slow_ptr = slow_ptr._next
 fast_ptr = fast_ptr._next._next

 if fast_ptr is None:
 # Even number of elements
 return (prev_ptr._element + slow_ptr._element) / 2
 else:
 # Odd number of elements
 return slow_ptr._element
