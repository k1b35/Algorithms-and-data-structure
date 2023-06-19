class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs(node):
    result = []  # список для хранения узлов в порядке обхода

    def dfs_recursive(node):
        if node is None:
            return

        result.append(node.value)  # добавляем текущий узел в список

        for child in node.children:  # рекурсивно обходим детей узла
            dfs_recursive(child)

    dfs_recursive(node)  # вызываем рекурсивную функцию для обхода дерева
    return result


# Пример использования
# Создаем дерево
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

root.children = [node2, node3]
node2.children = [node4, node5]
node3.children = [node6]

# Выполняем обход дерева в глубину (DFS)
result = dfs(root)
print(result)
