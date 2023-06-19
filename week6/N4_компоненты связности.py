def find_connected_components(graph):
    visited = set()  # Множество посещенных вершин
    components = []  # Список компонент

    def dfs(node, component):
        visited.add(node)
        component.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components


# Example
edges = [(1, 2), (2, 3), (4, 5), (6, 7), (7, 8)]
graph = {}


for edge in edges:
    u, v = edge
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

components = find_connected_components(graph)

print("Количество связных компонентов:", len(components))
print("Связные компоненты:")
for component in components:
    print(component)
