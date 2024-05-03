class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def put(self, key, value):
        index = hash(key) % self.size
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = hash(key) % self.size
        if self.table[index] is None:
            return None
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = hash(key) % self.size
        if self.table[index] is None:
            return None
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        return None

# Example usage
hash_table = HashTable(10)
hash_table.put("key1", "value1")
hash_table.put("key2", "value2")
print(hash_table.get("key1"))  # Output: value1
hash_table.remove("key1")
print(hash_table.get("key1"))  # Output: None
