def distance(x1, y1, x2, y2):
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    return length

print(distance(1, 2, 10 , 15))
