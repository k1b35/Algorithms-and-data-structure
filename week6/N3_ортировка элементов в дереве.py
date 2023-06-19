class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_node(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)

    return root


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)


def sort_tree(root):
    sorted_tree = None

    def insert_sorted(node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = insert_sorted(node.left, value)
        else:
            node.right = insert_sorted(node.right, value)

        return node

    def inorder_traversal_sorted(node):
        nonlocal sorted_tree

        if node is not None:
            inorder_traversal_sorted(node.left)
            sorted_tree = insert_sorted(sorted_tree, node.value)
            inorder_traversal_sorted(node.right)

    inorder_traversal_sorted(root)
    return sorted_tree


# Example
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print("Исходное дерево:")
inorder_traversal(root)
print()

sorted_root = sort_tree(root)

print("Отсортированное дерево:")
inorder_traversal(sorted_root)
print()
