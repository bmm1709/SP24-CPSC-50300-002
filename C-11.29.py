class Node:
 def __init__(self, key):
 self.key = key
 self.left = None
 self.right = None
 self.height = 1

class AVLTree:
 def insert(self, root, key):
 if not root:
 return Node(key)
 elif key < root.key:
 root.left = self.insert(root.left, key)
 else:
 root.right = self.insert(root.right, key)

 root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
 balance = self.getBalance(root)

 if balance > 1:
 if key < root.left.key:
 return self.rightRotate(root)
 else:
 root.left = self.leftRotate(root.left)
 return self.rightRotate(root)

 if balance < -1:
 if key > root.right.key:
 return self.leftRotate(root)
 else:
 root.right = self.rightRotate(root.right)
 return self.leftRotate(root)

 return root

 def leftRotate(self, z):
 y = z.right
 T2 = y.left
 y.left = z
 z.right = T2
 z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
 y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 return y

 def rightRotate(self, z):
 y = z.left
 T3 = y.right
 y.right = z
 z.left = T3
 z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
 y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
 return y

 def getHeight(self, root):
 if not root:
 return 0
 return root.height

 def getBalance(self, root):
 if not root:
 return 0
 return self.getHeight(root.left) - self.getHeight(root.right)

 def inorder(self, root):
 if root:
 self.inorder(root.left)
 print(root.key, end=' ')
 self.inorder(root.right)

# Create tree and inserts
avl_tree = AVLTree()
root = None
elements = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]
for elem in elements:
 root = avl_tree.insert(root, elem)

# Perform in-order traversal to retrieve sorted elements
print("Sorted elements:")
avl_tree.inorder(root)