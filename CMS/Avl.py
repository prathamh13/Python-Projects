from Node import Node

class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rebalance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, node, key, value):
        if not node:
            return Node(key, value)
        if key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.right = self.insert(node.right, key, value)

        return self.rebalance(node)

    def delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = self.get_min(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self.delete(node.right, temp.key)

        return self.rebalance(node)

    def get_min(self, node):
        while node.left:
            node = node.left
        return node

    def find(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    # Public methods
    def insert_key_value(self, key, value):
        self.root = self.insert(self.root, key, value)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def find_key(self, key):
        return self.find(self.root, key)

    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append((node.key, node.value))
        self.inorder(node.right, res)

    def get_all(self):
        res = []
        self.inorder(self.root, res)
        return res
