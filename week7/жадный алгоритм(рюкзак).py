items = [
    {"name": "item1", "w": 1, "v": 5},
    {"name": "item1", "w": 3, "v": 1},
    {"name": "item1", "w": 2, "v": 2},
    {"name": "item1", "w": 4, "v": 4},
    {"name": "item1", "w": 5, "v": 3},
    {"name": "item1", "w": 7, "v": 6},
    {"name": "item1", "w": 9, "v": 7}
]
def max_true_w(max_value, result):
    return max_value - sum([elem['w'] for elem in result])

max_w = 10
item_sort = sorted(items, key=lambda x: x['v']/x['w'])
print(item_sort)
result = []
for elem in item_sort:
    if elem['w'] <= max_true_w(max_w, result):
        result.append(elem)

w_total = 0
v_total = 0
for elem in result:
    print(elem['name'])
    w_total += elem['w']
    v_total += elem['v']

print('w_total', w_total)
print('v_total', v_total)
