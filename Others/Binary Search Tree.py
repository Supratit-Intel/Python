class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        def _min_value_node(n):
            current = n
            while current.left:
                current = current.left
            return current
        def _delete(node, key):
            if node is None:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = _min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node
        self.root = _delete(self.root, key)

if __name__ == '__main__':
    bst = BST()
    for v in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(v)
    print(bst.search(40))
    bst.delete(20)
    print(bst.search(20))