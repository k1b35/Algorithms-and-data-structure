def more_than_five(lst):
    l2 = []
    for i in range(len(lst)):
        if abs(lst[i]) > 10:
            l2.append(lst[i])
    return l2

print(more_than_five(lst = [1, 5, 77, -68, 13, 5, 8]))