import random
import time

def linear_search(arr):
    min_num = arr[0]
    max_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

def binary_search(arr):
    def find_min_max(left, right):
        if left == right:
            return arr[left], arr[left]
        elif left + 1 == right:
            return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
        else:
            mid = (left + right) // 2
            min1, max1 = find_min_max(left, mid)
            min2, max2 = find_min_max(mid + 1, right)
            return min(min1, min2), max(max1, max2)

    return find_min_max(0, len(arr) - 1)


arr = [random.randint(1, 10000000) for _ in range(10000000)]


start_time = time.time()
min_num_linear, max_num_linear = linear_search(arr)
linear_search_time = time.time() - start_time


start_time = time.time()
min_num_binary, max_num_binary = binary_search(arr)
binary_search_time = time.time() - start_time


print("Минимальное число (линейный поиск):", min_num_linear)
print("Максимальное число (линейный поиск):", max_num_linear)
print("Время выполнения (линейный поиск):", linear_search_time)

print("Минимальное число (бинарный поиск):", min_num_binary)
print("Максимальное число (бинарный поиск):", max_num_binary)
print("Время выполнения (бинарный поиск):", binary_search_time)
