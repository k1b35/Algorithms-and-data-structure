one = int(input())
two = int(input())


def roman():
    global one
    global two
    three = one + two
    return three


all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
             (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def to_roman(num):
    roman = ''
    while num > 0:
        for i, r in all_roman:
            while num >= i:
                roman += r
                num -= i
    return roman


three = roman()
# print(one)
# print(two)
# print(three)
one = to_roman(one)
two = to_roman(two)
three = to_roman(three)

print(one)
print(two)
print(three)
