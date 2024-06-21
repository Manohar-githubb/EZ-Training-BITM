class Node:
    def _init_(self, data):
        self.value = data
        self.left = None
        self.right = None

def bst(value, root):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = bst(value, root.left)
    else:
        root.right = bst(value, root.right)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

if __name__ == "__main__":
    root = None
    li = [90, 80, 70, 60, 50, 40, 30, 20, 10]
    for i in li:
        root = bst(i, root)
    inorder(root)
    print()