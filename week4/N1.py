import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


lists = []
for i in range(10):
    length = random.randint(1000, 10000)
    lst = [random.randint(1, 1000) for i in range(length)]
    lists.append(lst)

bubble_sort_times = []
for lst in lists:
    start_time = time.time()
    bubble_sort(lst)
    end_time = time.time()
    elapsed_time = end_time - start_time
    bubble_sort_times.append(elapsed_time)

sorted_times = []
for lst in lists:
    start_time = time.time()
    sorted(lst)
    end_time = time.time()
    elapsed_time = end_time - start_time
    sorted_times.append(elapsed_time)

print("Bubble Sort Times:", bubble_sort_times)
print("Sorted Times:", sorted_times)

# заметим, что встроенная функция sorted справляется гораздо быстрее
