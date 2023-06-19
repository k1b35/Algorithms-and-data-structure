n = int(input())

path = [(2, 1)]  # n==1

for i in range(1, n):
    path.append(((path[i - 1][0] - path[i - 1][1]) * 2 + path[i - 1][1] * 1, path[i - 1][0] - path[i - 1][1]))
    # print(path)

print(path[-1][1])
