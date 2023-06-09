# Считываем количество наборов данных
n = int(input())

for i in range(n):
  # Считываем строки с буквами
  first_line = input().split()
  second_line = input().split()

  # Преобразуем строки в множества для удобства поиска общих элементов
  first_set = set(first_line)
  second_set = set(second_line)

  # Находим общие элементы и выводим их без повторений
  common_elements = first_set.intersection(second_set)
  print(" ".join(set(common_elements)))