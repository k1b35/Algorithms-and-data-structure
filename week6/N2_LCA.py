class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    if root is None or node1 is None or node2 is None:
        return None

    # Если один из узлов равен корневому узлу, то корневой узел является LCA
    if root.value == node1.value or root.value == node2.value:
        return root

    # Рекурсивно ищем LCA в левом поддереве и правом поддереве
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # Если оба узла находятся в разных поддеревьях, то корневой узел является LCA
    if left_lca is not None and right_lca is not None:
        return root

    # Если один из узлов находится в левом поддереве, а другой в правом, то найденный узел является LCA
    if left_lca is not None:
        return left_lca
    if right_lca is not None:
        return right_lca

    # Если ни один из случаев выше не выполнен, значит оба узла находятся в одном поддереве
    # Возвращаем найденный LCA в поддереве
    return None

# Пример использования
# Создаем дерево
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

# Задаем узлы, для которых нужно найти LCA
node1 = node4
node2 = node5

# Выполняем поиск LCA
lca = find_lca(root, node1, node2)

# Выводим результат
if lca is not None:
    print("LCA:", lca.value)
else:
    print("Узлы не существуют")
