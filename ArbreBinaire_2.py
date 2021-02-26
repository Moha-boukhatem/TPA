class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                self.left.parent = self
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                self.right.parent = self
            else:
                self.right.insert(data)

    
    def get(self, data):
        if data < self.data:
            return self.left.get(data) if self.left else None
        elif data > self.data:
            return self.right.get(data) if self.right else None
        return self

    def __getitem__(self, key):
        node = self.get(key)
        if node:
            return node
        raise KeyError(key)

    def min(self):
        node = self
        while node.left:
            node = node.left
        return node

    def max(self):
        node = self
        while node.right:
            node = node.right
        return node
    
    def count_children(self):
        return bool(self.left) + bool(self.right)

    def is_left_child(self):
        return self.parent and self is self.parent.left

    def is_right_child(self):
        return self.parent and self is self.parent.right

    def get_successor(self):
        if self.right:
            return self.right.min()
        node = self
        while node.is_right_child():
            node = node.parent
        return node.parent

    def get_predecessor(self):
        if self.left:
            return self.left.max()
        node = self
        while node.is_left_child():
            node = node.parent
        return node.parent

    
    def delete(self, data):

        node = self.get(data)

        if not node:
            return

        children_count = node.count_children()

        if children_count == 0:
            if node.is_left_child():
                node.parent.left = None
            else:
                node.parent.right = None
            del node

        elif children_count == 1:
            child = node.left or node.right
            if node.is_left_child():
                node.parent.left = child
                child.parent = node.parent
                del node
            elif node.is_right_child():
                node.parent.right = child
                child.parent = node.parent
                del node
            else:
                root = node
                root.data = child.data
                root.left = child.left
                root.right = child.right
                if child.left:
                    child.left.parent = root
                if child.right:
                    child.right.parent = root
                del child

        else:
            succ = node.get_successor()
            node.data = succ.data
            if succ.is_left_child():
                succ.parent.left = succ.right
            else:
                succ.parent.right = succ.right
            if succ.right:
                succ.right.parent = succ.parent
            del succ



    def get_height(self):
        return 1 + max(
        self.left.get_height() if self.left else -1,
        self.right.get_height() if self.right else -1
        )

    def is_valid(self):
        prev = None
        for data in self:
            if prev and prev > data:
                return False
            prev = data
        return True


    def is_balanced(self):
        try:
            self._check_balance()
            return True
        except ValueError:
            return False

bst = Node(12) 
bst.insert(6)
bst.insert(14)


node = bst.get(9)

