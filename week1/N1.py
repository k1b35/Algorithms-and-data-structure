import sys

lines = sys.stdin.read()
print(lines)
bottles = []
bottles = lines.split('-1')
print(bottles)
# N = len(bottles)
# print(N)
# l = [map(lambda i: bottles[i].split('\n'), range(N))]
bottles = [bottles[i][0:(len(bottles[i]) - 1)] for i in range(len(bottles))]
l = [bottles[i].split('\n') for i in range(len(bottles))]
# print(l)
result = []
for i in range(len(l)):
    for j in range(len(l[i])):
        result.append(l[i][j])
print(result)


for i in range(len(l)):
    current_container = l[i]
    for j in range(len(l)):
        for k in range(len(l[j])):
            if l[j][k] in l[i]:
                q = result.find(str(l[j][k]))
                result.remove(q)

print(result)