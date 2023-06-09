def reverse_list(l):
    l2 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l2.append(l[i])
        else:
            l2.append(l[-i])
    return (l2)


print(reverse_list(l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
