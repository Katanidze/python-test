class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def compare(self, new_value):
        if new_value >= self.value:
            if self.right:
                self.right.compare(new_value)
            else:
                self.right = Node(new_value)
        if new_value < self.value:
            if self.left:
                self.left.compare(new_value)
            else:
                self.left = Node(new_value)
    def sort(self):
        if self.left:
            self.left = self.left.sort()
        else:
            self.left = []
        if self.right:
            self.right = self.right.sort()
        else:
            self.right = []
        return self.left + [self.value] + self.right

class SortedTree(object):
    def __init__(self):
        self.root = None
    def push(self, value):
        if self.root:
            self.root.compare(value)
        else:
            self.root = Node(value)
    def merge(self):
        return self.root.sort()

items = [7,4,11,2,6,3,8,12,9,10,1,5,13]
print(items)
tree = SortedTree()
for value in items:
    tree.push(value)

print(tree.merge())