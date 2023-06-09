def reverse_list(l):
    l2 = []
    for i in range(1, len(l) + 1):
    # for i in enumerate(l):
        l2.append(l[-i])
    return (l2)


print(reverse_list(l = [8, 1, 0, 4, 56, 78, 90]))
