def sort_array(nums):

    even_nums = []
    odd_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)


    even_nums.sort()

    odd_nums.sort(reverse=True)


    sorted_nums = even_nums + odd_nums

    return sorted_nums



import random


nums = random.sample(range(1, 101), 10)
print("Исходный массив:", nums)


sorted_nums = sort_array(nums)
print("Отсортированный массив:", sorted_nums)


sorted_nums_check = sorted(nums)
print(" встроенный метода сортировки:", sorted_nums_check)


if sorted_nums == sorted_nums_check:
    print("правильно.")
else:
    print("массивы различаются")
