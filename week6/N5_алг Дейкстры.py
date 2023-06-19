import heapq


def dijkstra(graph, start):
    distances = {}  # Словарь для хранения расстояний от начальной вершины
    queue = []  # Очередь с приоритетами для выбора вершин

    # Инициализация расстояний
    for vertex in graph:
        if vertex == start:
            distances[vertex] = 0
        else:
            distances[vertex] = float('inf')

        # Добавляем вершины в очередь с приоритетами
        heapq.heappush(queue, (distances[vertex], vertex))

    while queue:
        # Извлекаем вершину с наименьшим расстоянием
        current_distance, current_vertex = heapq.heappop(queue)

        # Если найдено более короткое расстояние до текущей вершины, обновляем его
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседних вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Пример использования
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3)
]

graph = {}
for u, v, w in edges:
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
    graph[v][u] = w

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print("Кратчайшие пути от вершины", start_vertex)
for vertex, distance in distances.items():
    print(f"Вершина {vertex}: Расстояние = {distance}")
