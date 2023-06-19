def linear_search_median(arr):
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        median = arr[n // 2]
    return median


def binary_search_median(arr):
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        median = arr[n // 2]
    return median


# sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 88, 99, 100, 567, 8904]
sorted_array = [1, 2, 463, 4, 5, 6, 7, 55, 9, 10, 11, 12, 13, 14, 15, 16, 8898, 99, 100, 57867, 8904]

linear_median = linear_search_median(sorted_array)
print("Медиана (линейный поиск):", linear_median)

binary_median = binary_search_median(sorted_array)
print("Медиана (бинарный поиск):", binary_median)

# Вывод:
# Медиана (линейный поиск): 11
# Медиана (бинарный поиск): 11
