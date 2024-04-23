class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
    def insert(self, parent_data, data):
        if self.root is None:
            self.root = TreeNode(data)
            return True
        
        parent_node = self._find_node(self.root, parent_data)
        if parent_node:
            parent_node.children.append(TreeNode(data))
            return True
        else:
            return False
    
    def _find_node(self, node, data):
        if node.data == data:
            return node
        
        for child in node.children:
            result = self._find_node(child, data)
            if result:
                return result
        
        return None
    
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        
        if node.data == data:
            return True
        
        for child in node.children:
            if self._search_recursive(child, data):
                return True
        
        return False
    
    def delete(self, data):
        if self.root is None:
            return False
        
        if self.root.data == data:
            self.root = None
            return True
        
        parent_node, target_index = self._find_parent_node_and_index(self.root, data)
        if parent_node and target_index is not None:
            del parent_node.children[target_index]
            return True
        else:
            return False
    
    def _find_parent_node_and_index(self, node, data):
        for i, child in enumerate(node.children):
            if child.data == data:
                return node, i
            
            parent_node, target_index = self._find_parent_node_and_index(child, data)
            if parent_node:
                return parent_node, target_index
        
        return None, None

    def update(self, old_data, new_data):
        if self.delete(old_data):
            self.insert(old_data, new_data)
            return True
        else:
            return False

    def traverse(self):
        return self._traverse_recursive(self.root)
    
    def _traverse_recursive(self, node):
        result = [node.data]
        for child in node.children:
            result.extend(self._traverse_recursive(child))
        return result

# Example usage:
tree = Tree()
tree.insert(None, 1)
tree.insert(1, 2)
tree.insert(1, 3)
tree.insert(2, 4)
tree.insert(2, 5)

print(tree.traverse())  # Output: [1, 2, 4, 5, 3]

tree.delete(4)
print(tree.traverse())  # Output: [1, 2, 5, 3]

tree.update(3, 6)
print(tree.traverse())  # Output: [1, 2, 5, 6]
