def select_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    selected_tasks = []
    end_time = float('-inf')

    for task in sorted_tasks:
        if task[0] >= end_time:
            selected_tasks.append(task)
            end_time = task[1]
    return selected_tasks


tasks = [(1, 3), (2, 4), (5, 7), (4, 6), (8, 9), (6, 10)]

selected = select_tasks(tasks)
print(selected)
