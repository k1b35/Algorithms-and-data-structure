import random


def sort_array(nums):
    # Используем сортировку пузырьком для сортировки массива
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break

    return nums


# Генерируем случайный массив из N положительных целых чисел
N = 10
nums = random.sample(range(1, 10 ** 6 + 1), N)
print(" массив:", nums)


sorted_nums = sort_array(nums)
print("Отсортированный массив:", sorted_nums)


sorted_nums_check = sorted(nums)
print("метода сортировки:", sorted_nums_check)


if sorted_nums == sorted_nums_check:
    print("верно")
else:
    print("неверно")
