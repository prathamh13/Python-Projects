class Node:
    def __init__(self, key, value):
        self.key = key  # typically a tuple (remaining_capacity, bin_id) or object_id
        self.value = value  # bin or object reference
        self.height = 1
        self.left = None
        self.right = None
